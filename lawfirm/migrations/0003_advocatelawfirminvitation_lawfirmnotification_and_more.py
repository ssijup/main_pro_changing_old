# Generated by Django 4.2.2 on 2023-09-22 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_remove_advocate_age_advocate_date_of_birth'),
        ('lawfirm', '0002_alter_lawfirm_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvocateLawfirmInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advocate_status', models.BooleanField(default=True)),
                ('invitation_status', models.BooleanField(default=False)),
                ('advocate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.advocate')),
                ('lawfirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawfirm.lawfirm')),
            ],
        ),
        migrations.CreateModel(
            name='LawfirmNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('lawfirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawfirm.lawfirm')),
            ],
        ),
        migrations.DeleteModel(
            name='AdvocateLawfirm',
        ),
    ]
