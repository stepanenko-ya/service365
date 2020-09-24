from django.shortcuts import render
from main.models import Order


def home(request):
    if request.method == "POST":
        x = request.POST.get("search_order")
        if x:
            result = Order.objects.filter(id=x).first()

    print(request.user.is_anonymous)

    if request.user.is_anonymous == False:
        xxx = request.user.groups.all()[0].name

    return render(request, "home/home.html", locals())

