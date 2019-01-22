# Generated by Django 2.0.5 on 2019-01-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('preferred_location', models.CharField(max_length=50)),
            ],
        ),
    ]
