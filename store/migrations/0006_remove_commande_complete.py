# Generated by Django 3.1.7 on 2021-04-05 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210405_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='complete',
        ),
    ]