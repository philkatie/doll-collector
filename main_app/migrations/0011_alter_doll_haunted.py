# Generated by Django 4.0.4 on 2022-04-26 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_doll_haunted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doll',
            name='haunted',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=('True', 'True'), max_length=5),
        ),
    ]
