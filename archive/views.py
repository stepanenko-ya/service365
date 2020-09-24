from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from main.models import Order, Status


@login_required
def archive(request):

    status = Status.objects.get(status="Выдан")
    done = Order.objects.filter(order_status=status)[::-1]

    return render(request, "archive/archive.html", locals())


def client_order(request):
    # orders = Order.objects.filter(id=)
    return render(request, "archive/client_order.html", locals())
