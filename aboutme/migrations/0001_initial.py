# Generated by Django 2.2.6 on 2020-06-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('pic', models.ImageField(upload_to='static/img')),
                ('description', models.TextField()),
            ],
        ),
    ]
