# Generated by Django 3.1.7 on 2021-03-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0014_auto_20210311_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologypage',
            name='x_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
