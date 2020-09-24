from django.urls import path
from. import views

urlpatterns = [
    path("archive/", views.archive, name="archive"),
    path("client_order/", views.client_order, name="client_order")
]