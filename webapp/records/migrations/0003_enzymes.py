# Generated by Django 4.1 on 2022-09-03 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_alter_cbc_test_units'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enzymes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=80)),
                ('results', models.FloatField(blank=True, null=True)),
                ('test_units', models.CharField(max_length=200)),
                ('ref', models.CharField(max_length=200, verbose_name='ref. values')),
                ('test_date', models.DateField()),
                ('patients_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.patient')),
            ],
        ),
    ]