# Generated by Django 3.1 on 2020-08-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200826_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='surname',
            field=models.CharField(blank=True, db_index=True, max_length=150),
        ),
    ]
