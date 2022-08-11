# Generated by Django 4.0.4 on 2022-08-10 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0011_rename_servidor_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impressora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Setor_do_Equipamento', models.CharField(max_length=100, null=True, verbose_name='Localização do DVR')),
                ('HostName', models.CharField(max_length=100, null=True, verbose_name='Host Name da Impressora')),
                ('Fabricante_do_Equipamento', models.CharField(choices=[('FAB', 'ESCOLHA UM FABRICANTE'), ('DLL', 'DELL'), ('HP', 'HEWLETT PACKARD'), ('SAM', 'SAMSUNG'), ('DTC', 'DATACARD'), ('CAN', 'CANON'), ('BEMAT', 'BEMATECH'), ('BROT', 'BROTHER'), ('ZB', 'ZEBRA')], default='FAB', max_length=50, null=True)),
                ('Modelo_do_Equipamento', models.CharField(choices=[('MODEL', 'MODELO DO EQUIPAMENTO'), ('M4080', 'M4080FX'), ('X4300', 'X4300LX'), ('ML-551', 'ML-551X'), ('4200TH', 'MP-4200TH'), ('8952DN', 'MFC-8952DN'), ('PLOTTER', 'IPF670 PLOTTER'), ('SD360', 'DATACARD SD360'), ('ZB110XI', 'ZB110XI'), ('ZB110XI4', '110XI4')], default='MODEL', max_length=20)),
                ('IP_Address', models.CharField(max_length=50, verbose_name='Endereço IP da Impressora')),
                ('Numero_Serie', models.CharField(max_length=50, verbose_name='Número de série da Impressora')),
            ],
        ),
        migrations.AlterField(
            model_name='server',
            name='Service_Tag',
            field=models.CharField(max_length=50, verbose_name='Service Tag do Servidor'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Setor_do_Equipamento',
            field=models.CharField(max_length=100, null=True, verbose_name='Localização do Servidor'),
        ),
        migrations.AlterField(
            model_name='server',
            name='Sistema_Operacional',
            field=models.CharField(choices=[('SOP', 'SELECIONE UM S.O'), ('WINS12', 'WINDOWS SERVER 2012 R2 DATACENTER'), ('WINS08', 'WINDOWS SERVER 2008 R2 ENTERPRISE')], default='SOP', max_length=50, null=True, verbose_name='Sistema operacional do Servidor'),
        ),
    ]
