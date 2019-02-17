# Generated by Django 2.0 on 2019-02-16 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0006_student_teacher'),
        ('dormadmin', '0002_auto_20190216_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormadminuser',
            name='incharge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admins', to='dorm.Building', verbose_name='Charge Building'),
        ),
        migrations.AlterField(
            model_name='dormadminuser',
            name='permission',
            field=models.IntegerField(verbose_name='Permission'),
        ),
    ]