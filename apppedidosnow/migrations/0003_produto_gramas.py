# Generated by Django 4.2.4 on 2023-08-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apppedidosnow", "0002_produto"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="gramas",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=7, null=True
            ),
        ),
    ]
