# Generated by Django 4.1.5 on 2023-02-09 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nse_app', '0006_pcr_option_remove_live_banknifty_at_set_pcr_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterModelTable(
            name='live',
            table='LiveSettings',
        ),
    ]
