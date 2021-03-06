# Generated by Django 2.0 on 2019-02-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0004_auto_20190216_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='building',
            name='number',
            field=models.IntegerField(unique=True, verbose_name='Building Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.CharField(default='', max_length=200, verbose_name='Student ID'),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('number', 'building')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('name', 'number')},
        ),
    ]
