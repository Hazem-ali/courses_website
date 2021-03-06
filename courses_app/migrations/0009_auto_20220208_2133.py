# Generated by Django 2.2 on 2022-02-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0008_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseimage',
            name='image_path',
            field=models.FileField(upload_to='course_images'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
