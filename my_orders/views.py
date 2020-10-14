from django.shortcuts import render


def my_orders(request):
    if request.user.is_anonymous == False:
        xxx = request.user.groups.all()[0].name

    return render(request, "my_orders/my_orders.html", locals())
