# Generated by Django 3.0.3 on 2020-02-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='type_task',
            field=models.CharField(default='inbox', max_length=64),
        ),
    ]
