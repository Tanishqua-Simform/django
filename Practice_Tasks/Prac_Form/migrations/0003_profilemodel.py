# Generated by Django 5.1.7 on 2025-03-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prac_Form', '0002_taskmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
