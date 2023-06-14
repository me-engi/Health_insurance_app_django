# Generated by Django 4.1 on 2023-06-05 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='insurance_photos/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('insurance_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='insurance_app.insuranceholder')),
            ],
        ),
    ]
