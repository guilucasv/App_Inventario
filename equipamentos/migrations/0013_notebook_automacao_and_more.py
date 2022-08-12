# Generated by Django 4.0.4 on 2022-08-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0012_impressora_alter_server_service_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook_Automacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HostName', models.CharField(max_length=100, null=True, verbose_name='Host Name do Notebook')),
                ('Fabricante_do_Equipamento', models.CharField(choices=[('FAB', 'ESCOLHA UM FABRICANTE'), ('DLL', 'DELL'), ('ACR', 'ACER'), ('POS', 'POSITIVO'), ('LEN', 'LENOVO'), ('HP', 'HEWLETT PACKARD'), ('AC', 'AOC'), ('SAM', 'SAMSUNG'), ('PHIL', 'PHILIPS')], default='FAB', max_length=50, null=True)),
                ('Modelo_do_Equipamento', models.CharField(choices=[('MODEL', 'MODELO DO EQUIPAMENTO'), ('E6430', 'LATITUDE E6430'), ('3420', 'LATITUDE 3420'), ('330-15IKB', 'IDEAPAD 330-15IKB'), ('3468', 'VOSTRO 14 3468'), ('A315-53-3470', 'ASPIRE 3 A315-53-3470'), ('5480', 'LATITUDE 5480'), ('VT5480', 'VOSTRO 5480'), ('HPG7', 'HP 240 G7'), ('3470', 'LATITUDE 3470'), ('VT5481', 'VOSTRO 5481'), ('3400', 'LATITUDE 3400'), ('LTE6430', 'LATITUDE E6430'), ('IPD3470', 'IDEAPAD 330-3470')], default='MODEL', max_length=20)),
                ('Usuario', models.CharField(max_length=50, null=True)),
                ('Licenca', models.CharField(choices=[('LVL', 'SELECIONE UM NÍVEL DE LICENÇA'), ('L1', 'LICENCA E1'), ('L2', 'LICENCA E2'), ('L3', 'LICENCA E3')], default='LVL', max_length=50)),
                ('Setor_do_Equipamento', models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], default='ESC', max_length=20)),
                ('Service_Tag', models.CharField(max_length=50, verbose_name='Service Tag do Notebook')),
                ('Mac_Address', models.CharField(max_length=50, verbose_name='Endereço MAC do Notebook')),
                ('IP_Adress', models.CharField(max_length=50, verbose_name='Endereço IP do Notebook')),
                ('Patrimônio', models.CharField(max_length=50)),
                ('Processador', models.CharField(max_length=50)),
                ('Memória', models.CharField(max_length=50)),
                ('HD', models.CharField(max_length=50)),
                ('Sistema_Operacional', models.CharField(choices=[('SOP', 'SELECIONE UM S.O'), ('WIN10', 'WINDOWS 10 64BITS PROFESSIONAL'), ('WIN7', 'WINDOWS 7 64 BITS PROFESSIONAL')], default='SOP', max_length=50, null=True, verbose_name='Sistema operacional do Equipamento')),
                ('Key_Office', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='desktop',
            name='Setor_do_Equipamento',
            field=models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], max_length=20, verbose_name='Setor do Equipamento'),
        ),
        migrations.AlterField(
            model_name='dvr',
            name='Setor_do_Equipamento',
            field=models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], default='ESC', max_length=20),
        ),
        migrations.AlterField(
            model_name='impressora',
            name='Setor_do_Equipamento',
            field=models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], default='ESC', max_length=20),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='Setor_do_Equipamento',
            field=models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], default='ESC', max_length=20),
        ),
        migrations.AlterField(
            model_name='server',
            name='Setor_do_Equipamento',
            field=models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], default='ESC', max_length=20),
        ),
        migrations.AlterField(
            model_name='wyse',
            name='Setor_do_Equipamento',
            field=models.CharField(choices=[('ESC', 'ESCOLHA UM SETOR'), ('RH', 'RECURSOS HUMANOS'), ('TI', 'TEC. DA INFORMAÇÃO'), ('CIND', 'CONTROLES INDUSTRIAIS'), ('MP6', 'MÁQUINA DE PAPEL 6'), ('EXPAP', 'EXPEDIÇÃO DE PAPEL'), ('FAB', 'FABRICAÇÃO DE PAPEL'), ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'), ('PCM', 'PCM MANUTENÇÃO'), ('BIBL', 'BIBLIOTECA'), ('PAF', 'POSTO AVANÇADO FISCAL'), ('ENG', 'ENGENHARIA'), ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'), ('SUPRI', 'SUPRIMENTOS'), ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'), ('FRT', 'FROTA'), ('OFC', 'OFICINA CENTRALIZADA'), ('PRTPRIN', 'PORTARIA PRINCIPAL'), ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'), ('ALMOX', 'ALMOXARIFADO'), ('ADMIN', 'ADMINISTRATIVO - CORREDOR'), ('CONVER', 'CONVERSÃO ADM'), ('APAR', 'APARAS'), ('DIST', 'DISTRIBUIÇÃO'), ('MP3/4', 'MP3 E MP4'), ('MP5', 'MAQ. DE PAPEL 5'), ('MP6', 'MAQ. DE PAPEL 6')], default='ESC', max_length=20),
        ),
    ]
