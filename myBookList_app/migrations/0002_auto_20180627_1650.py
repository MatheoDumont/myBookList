# Generated by Django 2.0.6 on 2018-06-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBookList_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='deathDay',
            field=models.DateField(blank=True),
        ),
    ]
