# Generated by Django 4.2.6 on 2023-11-17 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='addition_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Addition Date'),
            preserve_default=False,
        ),
    ]
