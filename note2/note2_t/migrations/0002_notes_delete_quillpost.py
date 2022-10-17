# Generated by Django 4.1.2 on 2022-10-15 17:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note2_t', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='QuillPost',
        ),
    ]
