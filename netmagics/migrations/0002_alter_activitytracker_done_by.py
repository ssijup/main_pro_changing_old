# Generated by Django 4.1.4 on 2023-09-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netmagics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytracker',
            name='done_by',
            field=models.CharField(default='unknown', max_length=250),
        ),
    ]