# Generated by Django 2.2.24 on 2021-07-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer1', models.CharField(max_length=200)),
                ('answer2', models.CharField(max_length=200)),
            ],
        ),
    ]
