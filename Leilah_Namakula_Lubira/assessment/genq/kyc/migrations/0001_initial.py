# Generated by Django 4.2 on 2023-04-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('Date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone1', models.CharField(max_length=10)),
                ('phone2', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
