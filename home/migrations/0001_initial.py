# Generated by Django 3.1.3 on 2021-03-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('message', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
