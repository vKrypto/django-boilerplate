# Generated by Django 4.1.5 on 2023-01-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210411_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='token',
            field=models.CharField(default='4bd7e27a-f707-4184-8d95-2564c0359f12', max_length=36, unique=True),
        ),
    ]
