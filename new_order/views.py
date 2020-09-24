from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Order, Status
from .forms import OrderForm
from django.http import HttpResponseRedirect
import turbosmsua
t = turbosmsua.Turbosms('office222333', '123456')


@login_required
def new_order(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        in_the_work = Status.objects.get(status="В работе")

        if form.is_valid():
            x = form.save()
            status_client = x.order_status
            # if status_client == in_the_work:
            #     send_statuses = t.send_text("stepdevelop",
            #                                 [x.phone_number],
            #                                 "Ваша заявка с номером " + str(
            #                                     x.id) +
            #                                 "создана. Посмотреть ее статус Вы можете на нашем сайте.")
            #     # print(send_statuses)

            return HttpResponseRedirect("http://127.0.0.1:8000/main/")
    else:
        form = OrderForm()

    return render(request, "new_order/new_order.html", {"form": form})







