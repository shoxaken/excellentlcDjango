# Generated by Django 4.2.5 on 2023-09-27 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0016_student_tolov_student_arab_tolov_student_matem_tolov_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='tolov',
        ),
        migrations.RemoveField(
            model_name='student_arab',
            name='tolov',
        ),
        migrations.RemoveField(
            model_name='student_matem',
            name='tolov',
        ),
        migrations.RemoveField(
            model_name='student_mental',
            name='tolov',
        ),
        migrations.RemoveField(
            model_name='student_rus',
            name='tolov',
        ),
    ]
