# Generated by Django 4.1 on 2022-08-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]