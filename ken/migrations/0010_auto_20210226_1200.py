# Generated by Django 2.1.7 on 2021-02-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ken', '0009_joinus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='joinus',
        ),
    ]
