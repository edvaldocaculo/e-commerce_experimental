# Generated by Django 4.2.1 on 2023-05-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_variacao_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variacao',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
