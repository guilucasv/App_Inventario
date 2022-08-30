# -- Importação dos MODELS para o painel de ADMIN -- #
from django.contrib import admin
from equipamentos.models import *
class Desktops(admin.ModelAdmin):
    list_display = ('HostName', 'Modelo_do_Equipamento', 'Setor_do_Equipamento', 'HD', 'IP_Adress', 'Mac_Address', 'Patrimônio', 'Service_Tag', 'Usuario')
    list_display_links = ('Usuario', 'Modelo_do_Equipamento', 'Setor_do_Equipamento', 'IP_Adress', 'HD', 'Mac_Address', 'Patrimônio', 'Service_Tag')
    search_fields = ('HostName', 'IP_Adress', 'Mac_Address',)

class Notebooks(admin.ModelAdmin):
    list_display = ('HostName', 'Usuario', 'Setor_do_Equipamento', 'HD', 'IP_Adress', 'Mac_Address', 'Patrimônio', 'Service_Tag', 'Usuario')
    list_display_links = ('Usuario', 'Setor_do_Equipamento', 'IP_Adress', 'HD', 'Mac_Address', 'Patrimônio', 'Service_Tag')
    search_fields = ('HostName', 'IP_Adress', 'Mac_Address',)

class Wyses(admin.ModelAdmin):
    list_display = ('HostName', 'Modelo_do_Equipamento', 'Setor_do_Equipamento', 'Service_Tag', 'Mac_Address', 'IP_Adress', 'Patrimonio', 'Fabricante_do_Monitor', 'Patrimonio_do_Monitor')
    list_display_links = ('HostName', 'Setor_do_Equipamento', 'IP_Adress',)
    search_fields = ('HostName', 'IP_Adress', 'Mac_Address',)

class Switches(admin.ModelAdmin):
    list_display = ('IP_Address', 'Setor_do_Equipamento', 'Mac_Address', 'Modelo', 'Service_Tag', 'Qtd_de_Portas', 'Fabricante')
    list_display_links = ('IP_Address', 'Setor_do_Equipamento', 'Mac_Address',)
    search_fields = ('IP_Address', 'IP_Adress', 'Mac_Address',)


class Dvrs(admin.ModelAdmin):
    list_display = ('IP_Address', 'Setor_do_Equipamento', 'Mac_Address', 'Modelo', 'Service_Tag', 'Qtd_de_Portas', 'Fabricante')
    list_display_links = ('IP_Address', 'Setor_do_Equipamento', 'Mac_Address',)
    search_fields = ('IP_Address', 'IP_Adress', 'Mac_Address',)

class Servidores(admin.ModelAdmin):
    list_display = ('Setor_do_Equipamento', 'IP_Address', 'Service_Tag', 'Patrimonio', 'Memoria', 'HD', 'Sistema_Operacional')
    list_display_links = ('IP_Address', 'Memoria', 'HD')
    search_fields = ('Service_Tag', 'Patrimonio', 'IP_Address', 'Setor_do_Equipamento',)

class Impressoras(admin.ModelAdmin):
    list_display = ('Setor_do_Equipamento', 'IP_Address', 'HostName', 'Modelo_do_Equipamento', 'Setor_do_Equipamento', 'Numero_Serie')
    list_display_links = ('IP_Address', 'Setor_do_Equipamento', 'HostName')
    search_fields = ('HostName', 'IP_Address',)


class Notebooks_de_Automacao(admin.ModelAdmin):
    list_display = ('HostName', 'Usuario', 'Setor_do_Equipamento', 'HD', 'IP_Adress', 'Mac_Address', 'Patrimônio', 'Service_Tag', 'Usuario')
    list_display_links = ('Usuario', 'Setor_do_Equipamento', 'IP_Adress', 'HD', 'Mac_Address', 'Patrimônio', 'Service_Tag')
    search_fields = ('HostName', 'IP_Adress', 'Mac_Address',)

admin.site.register(Notebook, Notebooks)
admin.site.register(Desktop, Desktops)
admin.site.register(Wyse, Wyses)
admin.site.register(Switch, Switches)
admin.site.register(Dvr, Dvrs)
admin.site.register(Server, Servidores)
admin.site.register(Impressora, Impressoras)
admin.site.register(NotebooksDeAutomacoe, Notebooks_de_Automacao)