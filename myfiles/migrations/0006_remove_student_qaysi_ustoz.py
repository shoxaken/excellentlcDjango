# Generated by Django 4.2.5 on 2023-09-17 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_alter_teachertype_nomi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='qaysi_ustoz',
        ),
    ]