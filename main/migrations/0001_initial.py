# Generated by Django 3.1 on 2020-08-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, help_text='097...', max_length=10, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
