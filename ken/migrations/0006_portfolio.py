# Generated by Django 2.1.7 on 2021-02-10 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ken', '0005_remove_astroh_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
