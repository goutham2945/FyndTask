# Generated by Django 3.2 on 2021-05-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('director', models.CharField(max_length=500)),
                ('score', models.FloatField()),
                ('name', models.CharField(max_length=500)),
                ('genre', models.ManyToManyField(to='app.Genre')),
            ],
        ),
    ]
