from django.urls import path
from. import views

urlpatterns = [
    path("done_id/", views.done_id, name="done_id")
]
