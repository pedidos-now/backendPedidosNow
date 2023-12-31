# Generated by Django 4.2.4 on 2023-10-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "apppedidosnow",
            "0009_remove_bairro_descricao_bairro_preco_bairro_titulo_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="bairro",
            old_name="titulo",
            new_name="nome",
        ),
        migrations.RemoveField(
            model_name="bairro",
            name="preco",
        ),
        migrations.AddField(
            model_name="bairro",
            name="preco_entrega",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="status",
            field=models.IntegerField(
                choices=[
                    (1, "Produção"),
                    (2, "Pronto"),
                    (3, "Aguardando pagamento"),
                    (4, "Fechado"),
                ],
                default=1,
            ),
        ),
    ]
