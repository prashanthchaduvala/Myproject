# Generated by Django 2.2.2 on 2019-11-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resetpass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newpassword', models.IntegerField()),
                ('conformpassword', models.IntegerField()),
            ],
        ),
    ]
