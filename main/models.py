from django.db import models


class Device(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.status


class Coast(models.Model):
    method = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.method


class Service(models.Model):
    service = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.service


class Order(models.Model):
    name_client = models.CharField(max_length=50, null=True, blank=True)
    surname = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    serial_number = models.CharField(max_length=30, null=True, blank=True)
    device_type = models.ForeignKey(Device, on_delete=models.CASCADE,
                                    null=True, blank=True)
    # service_work = models.ManyToManyField(Service, blank=True)
    order_status = models.ForeignKey(Status, on_delete=models.CASCADE,
                                     null=True, blank=True)
    manager = models.CharField(max_length=30, null=True, blank=True)
    payment_method = models.ForeignKey(Coast, on_delete=models.CASCADE,
                                       null=True, blank=True)
    price = models.IntegerField(blank=True, null=True, default=0)
    comment = models.TextField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False,
                                   null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True,
                                   null=True, blank=True)
