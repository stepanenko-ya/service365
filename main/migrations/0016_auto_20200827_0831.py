# Generated by Django 3.1 on 2020-08-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_order_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]