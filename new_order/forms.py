from django import forms
from main.models import Order, Device, Service, Status, Coast


class OrderForm(forms.Form):
    name_client = forms.CharField(max_length=50, label='Имя клиента')
    surname = forms.CharField(max_length=50, label="Фамилия")
    phone_number = forms.CharField(max_length=13, label="Номер телефона: +380")
    device_type = forms.ModelChoiceField(queryset=Device.objects.all(),
                                         label="Вид устройства")
    serial_number = forms.CharField(max_length=14,
                                    label="Серийный номер устройства")
    service_work = forms.ModelChoiceField(queryset=Service.objects.all(),
                                          label="Вид работы")
    order_status = forms.ModelChoiceField(queryset=Status.objects.all(),
                                          label="Статус заказа")
    manager = forms.CharField(max_length=25, label="Менеджер")
    payment_method = forms.ModelChoiceField(queryset=Coast.objects.all(),
                                            label="Метод оплаты",
                                            required=False)
    price = forms.IntegerField(initial='0', label="К оплате")
    comment = forms.CharField(widget=forms.Textarea, required=False,            # required=False    ---- значит поле не обязательно к заполнению
                              label="Коментарий к заказу")

    # def clean_surname(self):
    #     name_client = self.cleaned_data["name_client"]
    #     surname = self.cleaned_data['surname']
    #     return surname

    def save(self):
        x = Order(**self.cleaned_data)
        x.save()
        return x
