# Generated by Django 2.2.1 on 2019-06-04 09:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_announcement_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
