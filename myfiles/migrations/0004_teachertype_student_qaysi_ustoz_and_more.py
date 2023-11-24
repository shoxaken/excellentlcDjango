# Generated by Django 4.2.5 on 2023-09-17 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_student_arab_student_matem_student_mental_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='qaysi_ustoz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_arab',
            name='qaysi_ustoz',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_matem',
            name='qaysi_ustoz',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_mental',
            name='qaysi_ustoz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_rus',
            name='qaysi_ustoz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myfiles.teachertype'),
            preserve_default=False,
        ),
    ]