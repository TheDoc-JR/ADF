# Generated by Django 4.1 on 2022-09-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_alter_cbc_ref_alter_cbc_test_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bch',
            name='ref',
            field=models.CharField(choices=[('(74 - 109)', '(74 - 109)'), ('(0.7 - 1.2)', '(0.7 - 1.2)'), ('(3.4 - 7.0)', '(3.4 - 7.0)')], default='', max_length=200, verbose_name='Reference values'),
        ),
        migrations.AlterField(
            model_name='bch',
            name='test_units',
            field=models.CharField(choices=[('mg/dL', 'mg/dL')], default='mg/dL', max_length=200, verbose_name='Units'),
        ),
    ]
