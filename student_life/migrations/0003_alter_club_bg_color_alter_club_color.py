# Generated by Django 4.2.2 on 2023-08-18 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_life', '0002_club_bg_color_club_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='bg_color',
            field=models.CharField(default='white', max_length=50),
        ),
        migrations.AlterField(
            model_name='club',
            name='color',
            field=models.CharField(default='black', max_length=50),
        ),
    ]
