# Generated by Django 2.2.1 on 2019-06-04 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='date_posted',
        ),
    ]
