# Generated by Django 4.1.4 on 2023-09-12 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0009_advocate_type_of_user'),
        ('lawfirm', '0003_lawfirmadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvocateLawfirm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advocate_status', models.BooleanField(default=False)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.advocate')),
            ],
        ),
    ]