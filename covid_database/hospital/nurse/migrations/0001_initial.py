# Generated by Django 3.1.2 on 2020-11-16 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NURSE_DETAILS',
            fields=[
                ('Nurse_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Super_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nurse.nurse_details')),
            ],
        ),
    ]
