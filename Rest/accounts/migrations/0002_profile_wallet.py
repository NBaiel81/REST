# Generated by Django 3.1.7 on 2021-03-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wallet',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
