# Generated by Django 2.0 on 2019-02-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormadmin', '0004_auto_20190216_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormadminuser',
            name='password',
            field=models.CharField(default='', max_length=200, verbose_name='Password'),
        ),
    ]