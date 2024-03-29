# Generated by Django 2.2.2 on 2019-06-27 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banco', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(blank=True, null=True)),
                ('parcelas', models.IntegerField()),
                ('tx_juros', models.FloatField(blank=True, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('criando_em', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('id_banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.Banco')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
    ]
