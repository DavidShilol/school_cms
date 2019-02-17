# Generated by Django 2.0 on 2019-02-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('sex', models.CharField(max_length=10, verbose_name='Sex')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('workid', models.CharField(max_length=200, verbose_name='Work Id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
