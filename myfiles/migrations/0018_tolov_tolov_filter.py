# Generated by Django 4.2.5 on 2023-09-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0017_remove_student_tolov_remove_student_arab_tolov_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tolov',
            name='tolov_filter',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
