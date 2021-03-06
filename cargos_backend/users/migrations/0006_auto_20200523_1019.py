# Generated by Django 2.2.6 on 2020-05-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0005_auto_20200523_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ManyToManyField(to='users.Position'),
        ),
    ]
