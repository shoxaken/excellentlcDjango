# Generated by Django 4.2.5 on 2023-09-28 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0018_tolov_tolov_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='TolovQilganYokiQilmaganType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='tolov',
            name='tolov_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.tolovqilganyokiqilmagantype'),
        ),
    ]