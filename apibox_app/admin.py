from django.contrib import admin
# registrar o modelo Box para que ele apareça na interface de administração do Django
from .models import Box
# faça para mostrar o nome e o número da caixa na interface de administração
class BoxAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')
    search_fields=('numero',)
admin.site.register(Box, BoxAdmin)

