# Generated by Django 2.2.6 on 2019-10-23 11:34

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20191021_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='编辑内容'),
        ),
    ]
