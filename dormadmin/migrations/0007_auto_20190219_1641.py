# Generated by Django 2.0 on 2019-02-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormadmin', '0006_dormadminuser_idcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dormadminuser',
            name='permission',
            field=models.IntegerField(default=0, verbose_name='Permission'),
        ),
    ]
