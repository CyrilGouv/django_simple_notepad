# Generated by Django 3.1.3 on 2020-11-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20201110_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='finish',
            field=models.BooleanField(default=False),
        ),
    ]
