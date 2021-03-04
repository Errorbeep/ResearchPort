# Generated by Django 3.1.5 on 2021-01-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(max_length=50)),
                ('proj_id', models.IntegerField()),
                ('contract_id', models.IntegerField()),
                ('proj_type', models.CharField(max_length=30)),
                ('endpoint', models.DateTimeField(auto_now=True)),
                ('charge_man', models.CharField(max_length=30)),
                ('charge_dept', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('delegated_dept', models.CharField(max_length=50)),
                ('contract_funds', models.IntegerField()),
                ('equip_funds', models.IntegerField()),
                ('check_date', models.DateTimeField()),
                ('valid_time', models.IntegerField()),
                ('money_in_1', models.IntegerField()),
                ('money_in_date_1', models.DateTimeField(auto_now=True)),
                ('money_in_2', models.IntegerField()),
                ('money_in_date_2', models.DateTimeField(auto_now=True)),
                ('money_in_3', models.IntegerField()),
                ('money_in_date_3', models.DateTimeField(auto_now=True)),
                ('money_in_4', models.IntegerField()),
                ('money_in_date_4', models.DateTimeField(auto_now=True)),
                ('proj_intro', models.CharField(max_length=100)),
                ('money_in_all', models.IntegerField()),
                ('accomplish', models.CharField(max_length=100)),
                ('participator_1', models.CharField(max_length=30)),
                ('participator_2', models.CharField(max_length=30)),
                ('participator_3', models.CharField(max_length=30)),
                ('participator_4', models.CharField(max_length=30)),
                ('participator_5', models.CharField(max_length=30)),
                ('participator_6', models.CharField(max_length=30)),
                ('participator_7', models.CharField(max_length=30)),
                ('participator_8', models.CharField(max_length=30)),
                ('participator_9', models.CharField(max_length=30)),
                ('participator_10', models.CharField(max_length=30)),
            ],
        ),
    ]