# Generated by Django 4.2.3 on 2023-07-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_alter_faculty_description_alter_faculty_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/directions_study', verbose_name='Ta‘lim yo‘nalishi foto'),
        ),
    ]
