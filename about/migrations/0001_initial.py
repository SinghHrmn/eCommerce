# Generated by Django 2.1.5 on 2019-01-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('aboutus_photo', models.ImageField(blank=True, upload_to='phots/%Y/%m/%d')),
            ],
        ),
    ]
