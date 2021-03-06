# Generated by Django 3.1.7 on 2021-03-08 03:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_advert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='content',
        ),
        migrations.RenameModel(
            old_name='Advert',
            new_name='HomeSelection',
        ),
        migrations.CreateModel(
            name='HomeSelectionOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.homeselection')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='homepage', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
