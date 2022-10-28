# Generated by Django 4.1.2 on 2022-10-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pftest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='correspondencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=50)),
                ('cr1', models.IntegerField()),
                ('cr2', models.IntegerField()),
                ('cr3', models.IntegerField()),
                ('cr4', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ocupaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('relation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tabla_relacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('mat1', models.IntegerField()),
                ('mat2', models.IntegerField()),
                ('mat3', models.IntegerField()),
                ('mat4', models.IntegerField()),
                ('hab1', models.IntegerField()),
                ('hab2', models.IntegerField()),
                ('hab3', models.IntegerField()),
                ('hab4', models.IntegerField()),
                ('val1', models.IntegerField()),
                ('val2', models.IntegerField()),
                ('val3', models.IntegerField()),
                ('val4', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tipos_ocupacionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='valores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]