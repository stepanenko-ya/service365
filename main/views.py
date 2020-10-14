from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from. models import Order, Status


@login_required
def main(request):

    done = Status.objects.get(status="Выдан")
    x = Order.objects.all()
    order = x.exclude(order_status=done)[::-1]
    ready = Status.objects.get(status="Готов")

    return render(request, "main/main.html", locals())
