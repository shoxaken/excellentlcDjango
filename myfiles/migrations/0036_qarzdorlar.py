# Generated by Django 4.2.2 on 2023-11-08 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0035_vip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qarzdorlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('qaysi_fan', models.CharField(max_length=100)),
                ('qaycha_tolov', models.PositiveIntegerField(max_length=100)),
                ('qolgan_tolov', models.PositiveIntegerField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('Qaysi_oy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.tolovtype')),
                ('qaysi_ustoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype')),
            ],
        ),
    ]
