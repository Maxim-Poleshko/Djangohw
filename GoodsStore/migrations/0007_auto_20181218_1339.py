# Generated by Django 2.1.4 on 2018-12-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodsStore', '0006_auto_20181218_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
