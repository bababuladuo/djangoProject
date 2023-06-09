# Generated by Django 4.1.7 on 2023-04-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('length', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('way', models.CharField(max_length=32)),
                ('locate', models.CharField(max_length=32)),
                ('package', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('weight', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]
