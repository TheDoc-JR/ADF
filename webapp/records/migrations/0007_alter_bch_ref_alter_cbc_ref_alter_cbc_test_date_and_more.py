# Generated by Django 4.1 on 2022-09-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_alter_patient_bd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bch',
            name='ref',
            field=models.CharField(max_length=200, verbose_name='Reference values'),
        ),
        migrations.AlterField(
            model_name='cbc',
            name='ref',
            field=models.CharField(max_length=200, verbose_name='Reference values'),
        ),
        migrations.AlterField(
            model_name='cbc',
            name='test_date',
            field=models.DateField(verbose_name='Test date'),
        ),
        migrations.AlterField(
            model_name='cbc',
            name='test_name',
            field=models.CharField(choices=[('RED BLOOD CELLS', 'RED BLOOD CELLS'), ('HEMOGLOBIN', 'HEMOGLOBIN'), ('HEMATOCRIT', 'HEMATOCRIT')], max_length=80, verbose_name='Test name'),
        ),
        migrations.AlterField(
            model_name='enzymes',
            name='ref',
            field=models.CharField(max_length=200, verbose_name='Reference values'),
        ),
    ]