# Generated by Django 5.1.7 on 2025-03-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prac_Form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
