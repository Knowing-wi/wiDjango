# Generated by Django 2.1 on 2019-10-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191021_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='index',
            field=models.IntegerField(default=99, verbose_name='分类排序'),
        ),
    ]
