# Generated by Django 3.2 on 2023-10-27 05:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_auto_20231027_0222'),
        ('careerAdviceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='careeradvice',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
