from django.shortcuts import render
from main.models import Order, Device, Status, Coast, Service
from new_order.forms import OrderForm
from django.shortcuts import redirect
import turbosmsua
t = turbosmsua.Turbosms('office222333', '123456')


def orders(request):

    devices = Device.objects.all()
    statuses = Status.objects.all()
    service_work = Service.objects.all()
    methods_payment = Coast.objects.all()
    in_the_work = Status.objects.get(status="В работе")
    ready = Status.objects.get(status="Готов")
    client_id = request.GET.get("name_id")
    client = Order.objects.get(id=client_id)
    current_status = client.order_status

    if request.method == "POST":
        client.name_client = request.POST.get("name_client")
        client.surname = request.POST.get("last_name")
        client.phone_number = request.POST.get("phone")
        client.serial_number = request.POST.get("serial_number")
        client.price = request.POST.get("coast")
        client.comment = request.POST.get("comment")
        # client.service_work = Service.objects.get(service=request.POST.get("service_work"))
        client.device_type = Device.objects.get(type=request.POST.get("device"))
        client.order_status = Status.objects.get(status=request.POST.get("status"))

        method = request.POST.get("method_point")                # получаем из фронта то что ввел пользователь


        if method and method != "---":                            # если он что то ввел,то
            method_object = Coast.objects.get(method=method)      # ищем достаем это из базы данных
        else:                                                     # если ничего не ввели то
            method_object = None                                  # присваеваем None

        client.payment_method = method_object                     # тогда записываем в БД ничего или то что нашли в БД
        client.save()

        if current_status != client.order_status and client.order_status == ready:

            t.balance()
            send_statuses = t.send_text("stepdevelop",
                                        [client.phone_number],
                                        "Ваш заказ готов.")
            print(send_statuses)

        return redirect("/main/")

    return render(request, 'orders/orders.html', locals())
