# Generated by Django 3.0.4 on 2020-03-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200328_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='category',
            field=models.CharField(default='normal', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='author',
            field=models.CharField(max_length=20),
        ),
    ]