# Generated by Django 2.2.6 on 2020-06-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('size', models.CharField(max_length=225)),
                ('price', models.CharField(max_length=225)),
            ],
        ),
    ]
