# Generated by Django 2.2.6 on 2020-06-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('more', models.TextField()),
                ('pic', models.ImageField(upload_to='static/img')),
            ],
        ),
    ]
