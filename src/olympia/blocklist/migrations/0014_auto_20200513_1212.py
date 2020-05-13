# Generated by Django 2.2.12 on 2020-05-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocklist', '0013_kintoimport_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='kinto_id',
            field=models.CharField(db_index=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='kintoimport',
            name='kinto_id',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
