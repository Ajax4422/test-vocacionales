# Generated by Django 4.1.2 on 2022-10-26 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pftest', '0003_personas_resultados'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
