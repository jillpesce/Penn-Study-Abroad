# Generated by Django 2.2.7 on 2019-12-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191210_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='urlName',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
