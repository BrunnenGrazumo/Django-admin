# Generated by Django 3.2.6 on 2021-08-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_auto_20210812_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Статья', 'Статья'), ('Новость', 'Новость')], default='Статья', max_length=16),
        ),
    ]
