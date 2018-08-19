# Generated by Django 2.1 on 2018-08-19 00:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('A', 'Audio'), ('V', 'Video')], max_length=1)),
                ('url', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('first_names', models.CharField(max_length=200)),
                ('last_names', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='clip',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.Media'),
        ),
        migrations.AddField(
            model_name='clip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galeria.User'),
        ),
    ]
