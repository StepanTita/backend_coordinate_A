# Generated by Django 2.2.5 on 2019-10-14 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField()),
                ('elevations', models.IntegerField()),
                ('positions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('elevation', models.IntegerField()),
                ('position', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('length', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('width', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargos_main.Storage')),
            ],
            options={
                'unique_together': {('row', 'elevation', 'position')},
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('length', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('width', models.DecimalField(decimal_places=2, default=1, max_digits=9)),
                ('description', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_dated', models.DateField(default=datetime.datetime.now)),
                ('rotatable', models.BooleanField(default=False)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargos_main.Cell')),
            ],
        ),
    ]
