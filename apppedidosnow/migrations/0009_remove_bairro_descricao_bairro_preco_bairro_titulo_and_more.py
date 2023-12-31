# Generated by Django 4.2.4 on 2023-10-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apppedidosnow", "0008_bairro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bairro",
            name="descricao",
        ),
        migrations.AddField(
            model_name="bairro",
            name="preco",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=7, null=True
            ),
        ),
        migrations.AddField(
            model_name="bairro",
            name="titulo",
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Produção"), (2, "Pronto"), (3, "Pago")], default=1
            ),
        ),
    ]
