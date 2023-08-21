# Generated by Django 4.2.4 on 2023-08-19 14:48

import announcement.filetools
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('template_document', models.FileField(blank=True, null=True, upload_to=announcement.filetools.filename_creation)),
            ],
        ),
    ]
