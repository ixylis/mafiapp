# Generated by Django 2.2.6 on 2019-10-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_auto_20191014_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='active',
        ),
        migrations.AlterField(
            model_name='item',
            name='owners',
            field=models.ManyToManyField(related_name='items', to='engine.Player'),
        ),
    ]
