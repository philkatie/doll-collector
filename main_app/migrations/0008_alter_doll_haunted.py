# Generated by Django 4.0.4 on 2022-04-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_doll_haunted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doll',
            name='haunted',
            field=models.BooleanField(),
        ),
    ]
