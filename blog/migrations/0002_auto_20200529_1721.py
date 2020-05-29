# Generated by Django 2.2.12 on 2020-05-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='untagged', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.CharField(default='none.jpg', max_length=200),
            preserve_default=False,
        ),
    ]