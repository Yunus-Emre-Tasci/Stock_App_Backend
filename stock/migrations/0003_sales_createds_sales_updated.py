# Generated by Django 4.1.6 on 2023-03-10 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='createds',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sales',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
