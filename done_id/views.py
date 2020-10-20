from django.shortcuts import render
from main.models import Order, Status, Coast


def done_id(request):
    t = Coast.objects.all()
    order_id = request.GET.get("name_id")
    order = Order.objects.get(id=order_id)



    return render(request, "done_id/done_id.html", locals())
