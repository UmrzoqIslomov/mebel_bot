# Generated by Django 4.1 on 2022-08-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0007_savat_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='savat',
            name='slug',
            field=models.SlugField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]