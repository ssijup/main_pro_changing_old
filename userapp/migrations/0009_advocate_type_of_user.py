# Generated by Django 4.1.4 on 2023-09-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_remove_advocate_type_of_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='type_of_user',
            field=models.CharField(choices=[('normal_advocate', 'Normal Advocate'), ('normal_admin', 'Normal Admin'), ('super_admin', 'Super Admin')], default='normal_advocate', max_length=255),
        ),
    ]