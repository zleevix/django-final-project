# Generated by Django 3.2.4 on 2021-06-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Python2104',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=50)),
                ('tuoi', models.IntegerField()),
                ('diachi', models.TextField()),
            ],
            options={
                'db_table': 'Python2104',
            },
        ),
    ]
