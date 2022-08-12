from django.db import models

class Desktop(models.Model):

    # -- ADIÇÃO DE CHOICES PARA PREENCHIMENTO DAS INFORMAÇÕES -- #

    MODELOS = (
        ('3010', 'OPTIPLEX 3010'),
        ('3020', 'OPTIPLEX 3020'),
        ('3040', 'OPTIPLEX 3040'),
        ('3050', 'OPTIPLEX 3050'),
        ('7010', 'OPTIPLEX 7010'),
        ('INSP3647', 'INSPIRON 3647'),
        ('D60', 'POSITIVO MASTER D60'),
        ('3080', 'OPTIPLEX 3080'),
    )

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )

    FABRICANTES = (
        ('FAB', 'ESCOLHA UM FABRICANTE'),
        ('DLL', 'DELL'),
        ('ACR', 'ACER'),
        ('POS', 'POSITIVO'),
        ('LEN', 'LENOVO'),
        ('HP', 'HEWLETT PACKARD'),
        ('AC', 'AOC'),
        ('PHIL', 'PHILIPS'),
    )

    SOPERACIONAL = (
        ('WIN10', 'WINDOWS 10 64BITS PROFESSIONAL'),
        ('WIN7', 'WINDOWS 7 64 BITS PROFESSIONAL'),
    )

    # MODELS DA APLICAÇÃO #

    HostName = models.CharField(max_length=100, null=True, verbose_name="Host Name do Desktop")
    Fabricante_do_Equipamento = models.CharField(max_length=50, choices=FABRICANTES, null=True, verbose_name="Fabricante do Equipamento")
    Modelo_do_Equipamento = models.CharField(max_length=20, choices=MODELOS, blank=False, null=False)
    Usuario = models.CharField(max_length=50, null=True)
    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, verbose_name="Setor do Equipamento")
    Service_Tag = models.CharField(max_length=50, verbose_name="Service Tag do Desktop")
    Mac_Address = models.CharField(max_length=50, verbose_name="Endereço MAC do Desktop")
    IP_Adress = models.CharField(max_length=50, verbose_name="Endereço IP do Desktop")
    Patrimônio = models.CharField(max_length=50)
    Processador = models.CharField(max_length=50)
    Memória = models.CharField(max_length=50)
    HD = models.CharField(max_length=50)
    Sistema_Operacional = models.CharField(max_length=50, choices=SOPERACIONAL, null=True,verbose_name="Sistema operacional do Equipamento")
    Fabricante_do_Monitor = models.CharField(max_length=50, choices=FABRICANTES, null=True, verbose_name="Fabricante do Monitor")
    Patrimônio_do_Monitor = models.PositiveBigIntegerField()


    def __str__(self):
        return self.HostName

class Notebook(models.Model):

    MODELOS = (
        ('MODEL', 'MODELO DO EQUIPAMENTO'),
        ('E6430', 'LATITUDE E6430'),
        ('3420', 'LATITUDE 3420'),
        ('330-15IKB', 'IDEAPAD 330-15IKB'),
        ('3468', 'VOSTRO 14 3468'),
        ('A315-53-3470', 'ASPIRE 3 A315-53-3470'),
        ('5480', 'LATITUDE 5480'),
        ('VT5480', 'VOSTRO 5480'),
        ('HPG7', 'HP 240 G7'),
        ('3470', 'LATITUDE 3470'),
        ('VT5481', 'VOSTRO 5481'),
        ('3400', 'LATITUDE 3400'),
        ('LTE6430', 'LATITUDE E6430'),
        ('IPD3470', 'IDEAPAD 330-3470'),

    )

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )

    FABRICANTES = (
        ('FAB', 'ESCOLHA UM FABRICANTE'),
        ('DLL', 'DELL'),
        ('ACR', 'ACER'),
        ('POS', 'POSITIVO'),
        ('LEN', 'LENOVO'),
        ('HP', 'HEWLETT PACKARD'),
        ('AC', 'AOC'),
        ('SAM', 'SAMSUNG'),
        ('PHIL', 'PHILIPS'),
    )

    SOPERACIONAL = (
        ('SOP', 'SELECIONE UM S.O'),
        ('WIN10', 'WINDOWS 10 64BITS PROFESSIONAL'),
        ('WIN7', 'WINDOWS 7 64 BITS PROFESSIONAL'),
    )

    OFFICE = (
        ('LVL', 'SELECIONE UM NÍVEL DE LICENÇA'),
        ('L1', 'LICENCA E1'),
        ('L2', 'LICENCA E2'),
        ('L3', 'LICENCA E3'),
    )

    HostName = models.CharField(max_length=100, null=True, verbose_name="Host Name do Notebook")
    Fabricante_do_Equipamento = models.CharField(max_length=50, choices=FABRICANTES, null=True, default='FAB')
    Modelo_do_Equipamento = models.CharField(max_length=20, choices=MODELOS, blank=False, null=False, default='MODEL')
    Usuario = models.CharField(max_length=50, null=True)
    Licenca = models.CharField(max_length=50, choices=OFFICE, blank=False, null=False, default='LVL')
    Funcao = models.CharField(max_length=50)
    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, default='ESC')
    Service_Tag = models.CharField(max_length=50, verbose_name="Service Tag do Notebook")
    Mac_Address = models.CharField(max_length=50, verbose_name="Endereço MAC do Notebook")
    IP_Adress = models.CharField(max_length=50, verbose_name="Endereço IP do Notebook")
    Patrimônio = models.CharField(max_length=50)
    Processador = models.CharField(max_length=50)
    Memória = models.CharField(max_length=50)
    HD = models.CharField(max_length=50)
    Sistema_Operacional = models.CharField(max_length=50, choices=SOPERACIONAL, null=True, default='SOP', verbose_name="Sistema operacional do Equipamento")
    Key_Office = models.CharField(max_length=100)

    def __str__(self):
        return self.HostName

class Wyse(models.Model):

    MODEL = (
        ('MODEL', 'MODELO DO EQUIPAMENTO'),
        ('TX0', 'WYSE TX0'),
        ('SX0', 'WYSE SX0'),
        ('N10D', 'WYSE N10D'),
    )

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )
    FABRICANTES = (
       ('FAB', 'ESCOLHA UM FABRICANTE'),
       ('DLL', 'DELL'),
       ('ACR', 'ACER'),
       ('POS', 'POSITIVO'),
       ('LEN', 'LENOVO'),
       ('HP', 'HEWLETT PACKARD'),
       ('AC', 'AOC'),
       ('SAM', 'SAMSUNG'),
       ('PHIL', 'PHILIPS'),
    )

    HostName = models.CharField(max_length=100, null=True, verbose_name="Host Name do Wyse")
    Fabricante_do_Equipamento = models.CharField(max_length=50, choices=FABRICANTES, null=True, default='FAB')
    Modelo_do_Equipamento = models.CharField(max_length=20, choices=MODEL, blank=False, null=False, default='MODEL')
    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, default='ESC')
    Service_Tag = models.CharField(max_length=50, verbose_name="Service Tag do Equipamento")
    Mac_Address = models.CharField(max_length=50, verbose_name="Endereço MAC do Switch")
    IP_Adress = models.CharField(max_length=50, verbose_name="Endereço IP do Switch")
    Patrimonio = models.CharField(max_length=50)
    Fabricante_do_Monitor = models.CharField(max_length=50, choices=FABRICANTES, null=True, default='FAB', verbose_name="Fabricante do Monitor")
    Patrimonio_do_Monitor = models.CharField(max_length=50)


    def __str__(self):
        return self.HostName

class Switch(models.Model):
    MODELOS = (
      ('MODEL', 'MODELO DO EQUIPAMENTO'),
      ('PWVRTX', 'POWEREDGE VRTX'),
      ('PWRM630', 'POWEREDGE - M6303'),
      ('R710', 'POWEREDGE R710'),
      ('2950', 'POWEREDGE 2950'),
    )

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )
    FABRICANTES = (
       ('FAB', 'ESCOLHA UM FABRICANTE'),
       ('DLL', 'DELL'),
       ('HP', 'HEWLETT PACKARD'),
       ('SAM', 'SAMSUNG'),
    )

    Setor_do_Equipamento = models.CharField(max_length=50)
    Fabricante = models.CharField(max_length=50)
    Modelo = models.URLField(max_length=100)
    Service_Tag = models.CharField(max_length=50)
    IP_Address = models.CharField(max_length=50, verbose_name="Endereço IP do Switch")
    Mac_Address = models.CharField(max_length=50, verbose_name="Endereço MAC do Switch")
    Qtd_de_Portas = models.IntegerField(verbose_name="Quantidade de Portas")


    def __str__(self):
        return self.Setor

class Dvr(models.Model):

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )

    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, default='ESC')
    HostName = models.CharField(max_length=100, null=True, verbose_name="Host Name do DVR")
    Fabricante = models.CharField(max_length=50)
    Modelo = models.CharField(max_length=100, null=True, verbose_name="Modelo do DVR")
    Qtd_de_Portas = models.CharField(max_length=10, null=True, verbose_name="Quantidade de Portas")
    HD = models.CharField(max_length=10, verbose_name="Capacidade do HD")
    Mac_Address = models.CharField(max_length=50, verbose_name="Endereço MAC do DVR")
    IP_Address = models.CharField(max_length=50, verbose_name="Endereço IP do DVR")
    Service_Tag = models.CharField(max_length=50)

    def __str__(self):
        return self.Setor

class Server(models.Model):

    MODELOS = (
       ('MODEL', 'MODELO DO EQUIPAMENTO'),
       ('PWVRTX', 'POWEREDGE VRTX'),
       ('PWRM630', 'POWEREDGE - M6303'),
       ('R710', 'POWEREDGE R710'),
       ('2950', 'POWEREDGE 2950'),
    )

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )
    FABRICANTES = (
       ('FAB', 'ESCOLHA UM FABRICANTE'),
       ('DLL', 'DELL'),
       ('HP', 'HEWLETT PACKARD'),
       ('SAM', 'SAMSUNG'),
    )

    SOPERACIONAL = (
       ('SOP', 'SELECIONE UM S.O'),
       ('WINS12', 'WINDOWS SERVER 2012 R2 DATACENTER'),
       ('WINS08', 'WINDOWS SERVER 2008 R2 ENTERPRISE'),
    )

    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, default='ESC')
    Fabricante_do_Equipamento = models.CharField(max_length=50, choices=FABRICANTES, null=True, default='FAB')
    Modelo_do_Equipamento = models.CharField(max_length=20, choices=MODELOS,  blank=False, null=False, default='MODEL')
    IP_Address = models.CharField(max_length=50, verbose_name="Endereço IP do Servidor")
    Patrimonio = models.CharField(max_length=50)
    Service_Tag = models.CharField(max_length=50, verbose_name="Service Tag do Servidor")
    Memoria = models.CharField(max_length=50)
    HD = models.CharField(max_length=50)
    Sistema_Operacional = models.CharField(max_length=50, choices=SOPERACIONAL, null=True, default='SOP', verbose_name="Sistema operacional do Servidor")


class Impressora(models.Model):
    SETORES = (
        ('ESC', 'ESCOLHA UM SETOR'),
        ('RH', 'RECURSOS HUMANOS'),
        ('TI', 'TEC. DA INFORMAÇÃO'),
        ('CIND', 'CONTROLES INDUSTRIAIS'),
        ('MP6', 'MÁQUINA DE PAPEL 6'),
        ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
        ('FAB', 'FABRICAÇÃO DE PAPEL'),
        ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
        ('PCM', 'PCM MANUTENÇÃO'),
        ('BIBL', 'BIBLIOTECA'),
        ('PAF', 'POSTO AVANÇADO FISCAL'),
        ('ENG', 'ENGENHARIA'),
        ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
        ('SUPRI', 'SUPRIMENTOS'),
        ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
        ('FRT', 'FROTA'),
        ('OFC', 'OFICINA CENTRALIZADA'),
        ('PRTPRIN', 'PORTARIA PRINCIPAL'),
        ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
        ('ALMOX', 'ALMOXARIFADO'),
        ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
        ('CONVER', 'CONVERSÃO ADM'),
        ('APAR', 'APARAS'),
        ('DIST', 'DISTRIBUIÇÃO'),
        ('MP3/4', 'MP3 E MP4'),
        ('MP5', 'MAQ. DE PAPEL 5'),
        ('MP6', 'MAQ. DE PAPEL 6'),
    )
    FABRICANTES = (
      ('FAB', 'ESCOLHA UM FABRICANTE'),
      ('DLL', 'DELL'),
      ('HP', 'HEWLETT PACKARD'),
      ('SAM', 'SAMSUNG'),
      ('DTC', 'DATACARD'),
      ('CAN', 'CANON'),
      ('BEMAT', 'BEMATECH'),
      ('BROT', 'BROTHER'),
      ('ZB', 'ZEBRA'),
    )
    MODELOS = (
      ('MODEL', 'MODELO DO EQUIPAMENTO'),
      ('M4080', 'M4080FX'),
      ('X4300', 'X4300LX'),
      ('ML-551', 'ML-551X'),
      ('4200TH', 'MP-4200TH'),
      ('8952DN','MFC-8952DN'),
      ('PLOTTER', 'IPF670 PLOTTER'),
      ('SD360', 'DATACARD SD360'),
      ('ZB110XI', 'ZB110XI'),
      ('ZB110XI4', '110XI4'),
    )
    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, default='ESC')
    HostName = models.CharField(max_length=100, null=True, verbose_name="Host Name da Impressora")
    Fabricante_do_Equipamento = models.CharField(max_length=50, choices=FABRICANTES, null=True, default='FAB')
    Modelo_do_Equipamento = models.CharField(max_length=20, choices=MODELOS,  blank=False, null=False, default='MODEL')
    IP_Address = models.CharField(max_length=50, verbose_name="Endereço IP da Impressora")
    Numero_Serie = models.CharField(max_length=50, verbose_name="Número de série da Impressora")


class NotebooksDeAutomacoe(models.Model):
    MODELOS = (
        ('MODEL', 'MODELO DO EQUIPAMENTO'),
        ('E6430', 'LATITUDE E6430'),
        ('3420', 'LATITUDE 3420'),
        ('330-15IKB', 'IDEAPAD 330-15IKB'),
        ('3468', 'VOSTRO 14 3468'),
        ('A315-53-3470', 'ASPIRE 3 A315-53-3470'),
        ('5480', 'LATITUDE 5480'),
        ('VT5480', 'VOSTRO 5480'),
        ('HPG7', 'HP 240 G7'),
        ('3470', 'LATITUDE 3470'),
        ('VT5481', 'VOSTRO 5481'),
        ('3400', 'LATITUDE 3400'),
        ('LTE6430', 'LATITUDE E6430'),
        ('IPD3470', 'IDEAPAD 330-3470'),
    )

    SETORES = (
       ('ESC', 'ESCOLHA UM SETOR'),
       ('RH', 'RECURSOS HUMANOS'),
       ('TI', 'TEC. DA INFORMAÇÃO'),
       ('CIND', 'CONTROLES INDUSTRIAIS'),
       ('MP6', 'MÁQUINA DE PAPEL 6'),
       ('EXPAP', 'EXPEDIÇÃO DE PAPEL'),
       ('FAB', 'FABRICAÇÃO DE PAPEL'),
       ('MANMEC', 'MANUTENÇÃO DE MECÂNICA'),
       ('PCM', 'PCM MANUTENÇÃO'),
       ('BIBL', 'BIBLIOTECA'),
       ('PAF', 'POSTO AVANÇADO FISCAL'),
       ('ENG', 'ENGENHARIA'),
       ('PCP', 'PLAN. E CONTROLE DA PRODUÇÃO'),
       ('SUPRI', 'SUPRIMENTOS'),
       ('FABCONV', 'FABRICAÇÃO DA CONVERSÃO'),
       ('FRT', 'FROTA'),
       ('OFC', 'OFICINA CENTRALIZADA'),
       ('PRTPRIN', 'PORTARIA PRINCIPAL'),
       ('EXPED', 'CARREGAMENTO EXPEDIÇÃO'),
       ('ALMOX', 'ALMOXARIFADO'),
       ('ADMIN', 'ADMINISTRATIVO - CORREDOR'),
       ('CONVER', 'CONVERSÃO ADM'),
       ('APAR', 'APARAS'),
       ('DIST', 'DISTRIBUIÇÃO'),
       ('MP3/4', 'MP3 E MP4'),
       ('MP5', 'MAQ. DE PAPEL 5'),
       ('MP6', 'MAQ. DE PAPEL 6'),
    )

    FABRICANTES = (
        ('FAB', 'ESCOLHA UM FABRICANTE'),
        ('DLL', 'DELL'),
        ('ACR', 'ACER'),
        ('POS', 'POSITIVO'),
        ('LEN', 'LENOVO'),
        ('HP', 'HEWLETT PACKARD'),
        ('AC', 'AOC'),
        ('SAM', 'SAMSUNG'),
        ('PHIL', 'PHILIPS'),
    )

    SOPERACIONAL = (
        ('SOP', 'SELECIONE UM S.O'),
        ('WIN10', 'WINDOWS 10 64BITS PROFESSIONAL'),
        ('WIN7', 'WINDOWS 7 64 BITS PROFESSIONAL'),
    )

    OFFICE = (
        ('LVL', 'SELECIONE UM NÍVEL DE LICENÇA'),
        ('L1', 'LICENCA E1'),
        ('L2', 'LICENCA E2'),
        ('L3', 'LICENCA E3'),
    )

    HostName = models.CharField(max_length=100, null=True, verbose_name="Host Name do Notebook")
    Fabricante_do_Equipamento = models.CharField(max_length=50, choices=FABRICANTES, null=True, default='FAB')
    Modelo_do_Equipamento = models.CharField(max_length=20, choices=MODELOS, blank=False, null=False, default='MODEL')
    Usuario = models.CharField(max_length=50, null=True)
    Licenca = models.CharField(max_length=50, choices=OFFICE, blank=False, null=False, default='LVL')
    Setor_do_Equipamento = models.CharField(max_length=20, choices=SETORES, null=False, default='ESC')
    Service_Tag = models.CharField(max_length=50, verbose_name="Service Tag do Notebook")
    Mac_Address = models.CharField(max_length=50, verbose_name="Endereço MAC do Notebook")
    IP_Adress = models.CharField(max_length=50, verbose_name="Endereço IP do Notebook")
    Patrimônio = models.CharField(max_length=50)
    Processador = models.CharField(max_length=50)
    Memória = models.CharField(max_length=50)
    HD = models.CharField(max_length=50)
    Sistema_Operacional = models.CharField(max_length=50, choices=SOPERACIONAL, null=True, default='SOP', verbose_name="Sistema operacional do Equipamento")
    Key_Office = models.CharField(max_length=100)

    def __str__(self):
        return self.HostName