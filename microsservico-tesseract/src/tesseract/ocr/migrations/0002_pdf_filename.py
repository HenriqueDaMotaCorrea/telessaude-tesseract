# Generated by Django 3.0.3 on 2020-02-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdf',
            name='filename',
            field=models.CharField(default='No file', max_length=200),
            preserve_default=False,
        ),
    ]
