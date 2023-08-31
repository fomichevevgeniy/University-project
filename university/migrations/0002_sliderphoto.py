# Generated by Django 4.2.3 on 2023-07-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/slider_photos', verbose_name='O‘quv jarayonidan lavha')),
            ],
            options={
                'verbose_name': 'Lavha',
                'verbose_name_plural': 'Lavhalar',
            },
        ),
    ]
