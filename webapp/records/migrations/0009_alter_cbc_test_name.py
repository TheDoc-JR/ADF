# Generated by Django 4.1 on 2022-09-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_alter_cbc_test_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbc',
            name='test_name',
            field=models.CharField(choices=[('RED BLOOD CELLS', 'Red Blood Cells'), ('HEMOGLOBIN', 'Hemoglobin'), ('HEMATOCRIT', 'Hematocrit')], default='', max_length=80, verbose_name='Test name'),
        ),
    ]