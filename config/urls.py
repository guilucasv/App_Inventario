from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('', TemplateView.as_view(template_name="analytics.html")),
]


#altera o texto do cabeçalho 'administração do Django'
admin.site.site_header = 'Inventário Carta Softys'    # default: "Django Administration"
admin.site.index_title = 'Inventário de Ativos Softys Anápolis'    # default: "Site administration"
admin.site.site_title = 'Inventário de Equipamentos Carta Sotfys' # default: "Django site admin"
