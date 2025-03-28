# Generated by Django 5.1.7 on 2025-03-25 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_alter_doctor_pathologies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='hourly_rate',
        ),
        migrations.AddField(
            model_name='doctor',
            name='value',
            field=models.IntegerField(blank=True, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='education',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='doctors.doctor'),
        ),
    ]
