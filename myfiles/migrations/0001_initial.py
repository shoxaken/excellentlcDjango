# Generated by Django 4.2.5 on 2023-09-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('yosh', models.PositiveIntegerField(max_length=100)),
                ('manzil', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
