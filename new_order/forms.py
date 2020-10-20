from django import forms
from main.models import Order, Device, Service, Status, Coast


class OrderForm(forms.Form):
    # name_client = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'new_order_field'}), label='Имя клиента', max_length=50)

    name_client = forms.CharField(max_length=50, label='Имя клиента' )
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'new_order_field'}), max_length=50, label="Фамилия")
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'new_order_field'}),
        max_length=13, label="Номер телефона: +380")
    device_type = forms.ModelChoiceField(queryset=Device.objects.all(),
                                         label="Вид устройства")
    serial_number = forms.CharField(max_length=14,
                                    label="Серийный номер устройства")
    service_work = forms.ModelMultipleChoiceField(queryset=Service.objects.all()
                                                  , label="Вид работы")
    order_status = forms.ModelChoiceField(queryset=Status.objects.all(),
                                          label="Статус заказа")
    manager = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'new_order_field'}), max_length=50, label='Менеджер')
    payment_method = forms.ModelChoiceField(queryset=Coast.objects.all(),
                                            label="Метод оплаты",
                                            required=False)
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "new_order_field"}), initial='0', label="К оплате")
    comment = forms.CharField(widget=forms.Textarea(                               # (attrs={"class": "имя класа для CSS"})
            attrs={"class": "comment"}), label="Коментарий", required=False)       # required=False- поле к заполнению не обязательно


                                           # ), required=False,
                                           #  label="Коментарий к заказу")
    def save(self):
        x = Order(**self.cleaned_data)
        x.save()
        return x


    # def clean_surname(self):
    #     name_client = self.cleaned_data["name_client"]
    #     surname = self.cleaned_data['surname']
    #     return surname


