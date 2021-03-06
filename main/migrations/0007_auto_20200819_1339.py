# Generated by Django 3.1 on 2020-08-19 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200819_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coast',
            old_name='price',
            new_name='method',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.coast'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
