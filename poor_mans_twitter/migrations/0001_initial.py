# Generated by Django 4.0.3 on 2022-04-06 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)])),
                ('message', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(50)])),
                ('pub_date', models.DateTimeField(verbose_name='publication date')),
            ],
            options={
                'ordering': ['-pub_date', 'username'],
            },
        ),
    ]
