# Generated by Django 2.0.5 on 2018-08-28 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content2', models.TextField()),
                ('content3', models.TextField()),
            ],
        ),
    ]
