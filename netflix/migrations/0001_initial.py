# Generated by Django 3.1.7 on 2021-03-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.DateField()),
                ('poster', models.ImageField(upload_to='movies/posters')),
                ('video', models.FileField(upload_to='movies/video')),
                ('categories', models.ManyToManyField(to='netflix.category')),
            ],
        ),
    ]
