# Generated by Django 4.2.5 on 2023-09-20 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0010_qayerdantanigantype_alter_student_oquv_tanigan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('qaysi_fan', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('qaysi_ustoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype')),
            ],
        ),
    ]
