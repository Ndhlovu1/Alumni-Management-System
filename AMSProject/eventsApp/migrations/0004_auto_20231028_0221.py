# Generated by Django 3.2 on 2023-10-28 02:21

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0003_alter_eventsapp_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventsapp',
            options={'ordering': ('-start_date',)},
        ),
        migrations.AlterModelManagers(
            name='eventsapp',
            managers=[
                ('publishedArticles', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='eventsapp',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
