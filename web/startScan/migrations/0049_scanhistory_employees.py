# Generated by Django 3.2.4 on 2021-06-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0048_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanhistory',
            name='employees',
            field=models.ManyToManyField(related_name='employees', to='startScan.Employee'),
        ),
    ]