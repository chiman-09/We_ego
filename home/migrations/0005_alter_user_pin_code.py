# Generated by Django 3.2.9 on 2021-12-05 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211205_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pin_code',
            field=models.CharField(default='', max_length=6),
        ),
    ]
