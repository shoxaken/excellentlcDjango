# Generated by Django 4.2.5 on 2023-09-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0013_tolovtype_tolov_qaysi_oy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juft_kunlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gurux_nomi', models.CharField(max_length=50)),
                ('gurux_vaqti', models.CharField(max_length=25)),
                ('qaysi_ustoz', models.CharField(max_length=25)),
                ('qaysi_fan', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Toq_kunlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gurux_nomi', models.CharField(max_length=50)),
                ('gurux_vaqti', models.CharField(max_length=25)),
                ('qaysi_ustoz', models.CharField(max_length=25)),
                ('qaysi_fan', models.CharField(max_length=25)),
            ],
        ),
    ]
