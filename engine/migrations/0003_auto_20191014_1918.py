# Generated by Django 2.2.6 on 2019-10-14 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20191014_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='owners',
        ),
        migrations.RemoveField(
            model_name='item',
            name='triggers',
        ),
        migrations.RemoveField(
            model_name='trigger',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='trigger',
            name='effect',
        ),
        migrations.RemoveField(
            model_name='trigger',
            name='item',
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.DeleteModel(
            name='Effect',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Trigger',
        ),
    ]
