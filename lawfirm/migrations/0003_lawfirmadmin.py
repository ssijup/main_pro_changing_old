# Generated by Django 4.1.4 on 2023-09-10 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lawfirm', '0002_alter_lawfirm_estd_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='LawfirmAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(default='2000-01-01')),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(default='not given', max_length=200)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('is_owner', models.BooleanField(default=False)),
                ('lawfirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lawfirm.lawfirm')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
