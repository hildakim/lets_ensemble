# Generated by Django 3.2.5 on 2021-08-05 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20210805_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver_id',
        ),
    ]
