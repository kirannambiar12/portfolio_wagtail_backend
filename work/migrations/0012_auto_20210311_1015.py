# Generated by Django 3.1.7 on 2021-03-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_auto_20210311_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fullstackpage',
            old_name='full_stack_description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='technologypage',
            name='technology_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
