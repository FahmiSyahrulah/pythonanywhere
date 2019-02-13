# Generated by Django 2.1.5 on 2019-02-13 07:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('tanggal', models.DateField(default=django.utils.timezone.now)),
                ('deskripsi', models.CharField(max_length=255)),
            ],
        ),
    ]
