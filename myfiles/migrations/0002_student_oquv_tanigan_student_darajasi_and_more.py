# Generated by Django 4.2.5 on 2023-09-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Oquv_tanigan',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='darajasi',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='dars_soati',
            field=models.PositiveIntegerField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='telefon',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='telefon2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
