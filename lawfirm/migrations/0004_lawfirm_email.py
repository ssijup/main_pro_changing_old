# Generated by Django 4.2.2 on 2023-09-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawfirm', '0003_advocatelawfirminvitation_lawfirmnotification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawfirm',
            name='email',
            field=models.EmailField(default='default@gmail.com', max_length=254),
        ),
    ]
