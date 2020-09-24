from django.forms import ModelForm
from main.models import Order


class XXXForm(ModelForm):
    class Meta:
        model: Order


