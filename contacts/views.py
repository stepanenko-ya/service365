from django.shortcuts import render


def contacts(request):
    if request.user.is_anonymous == False:
        xxx = request.user.groups.all()[0].name

    return render(request, "contacts/contacts.html", locals())
