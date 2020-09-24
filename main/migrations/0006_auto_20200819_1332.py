# Generated by Django 3.1 on 2020-08-19 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200819_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.coast'),
        ),
    ]