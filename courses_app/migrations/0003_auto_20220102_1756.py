# Generated by Django 2.2 on 2022-01-02 17:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_auto_20220101_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='rate',
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_app.Instructor')),
            ],
        ),
    ]
