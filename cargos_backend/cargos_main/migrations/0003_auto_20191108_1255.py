# Generated by Django 2.2.5 on 2019-11-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cargos_main', '0002_auto_20191106_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='default_height',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
        ),
        migrations.AddField(
            model_name='storage',
            name='default_length',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
        ),
        migrations.AddField(
            model_name='storage',
            name='default_width',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
        ),
    ]
