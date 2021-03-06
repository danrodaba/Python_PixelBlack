# Generated by Django 3.1.3 on 2020-11-14 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('texto', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
