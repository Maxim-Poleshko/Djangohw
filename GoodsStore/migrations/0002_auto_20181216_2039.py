# Generated by Django 2.1.4 on 2018-12-16 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodsStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='upload_img',
            field=models.FileField(upload_to='static/upload_img/'),
        ),
    ]
