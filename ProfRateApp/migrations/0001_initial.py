# Generated by Django 3.2.12 on 2022-03-17 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30)),
                ('taughtYear', models.IntegerField()),
                ('semester', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_year', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('Professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfRateApp.professors')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfRateApp.modules')),
            ],
        ),
        migrations.AddField(
            model_name='modules',
            name='taughtBy',
            field=models.ManyToManyField(to='ProfRateApp.Professors'),
        ),
    ]
