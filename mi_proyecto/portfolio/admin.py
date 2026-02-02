from django.contrib import admin
from .models import Perfil, Educacion, Experiencia, Habilidad


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'titulo', 'email', 'actualizado')
    search_fields = ('nombre', 'email')
    readonly_fields = ('creado', 'actualizado')
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'titulo', 'resumen')
        }),
        ('Contacto', {
            'fields': ('email', 'telefono', 'ubicacion')
        }),
        ('Multimedia', {
            'fields': ('foto',)
        }),
        ('Auditoría', {
            'fields': ('creado', 'actualizado'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'centro', 'anio_inicio', 'anio_fin', 'orden')
    list_editable = ('orden',)
    search_fields = ('titulo', 'centro')
    list_filter = ('anio_inicio', 'anio_fin')
    readonly_fields = ('creado',)


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fecha_inicio', 'fecha_fin', 'en_curso', 'orden')
    list_editable = ('en_curso', 'orden')
    search_fields = ('cargo', 'empresa')
    list_filter = ('fecha_inicio', 'en_curso')
    readonly_fields = ('creado',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('cargo', 'empresa', 'descripcion')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin', 'en_curso')
        }),
        ('Orden', {
            'fields': ('orden',)
        }),
        ('Auditoría', {
            'fields': ('creado',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'nivel', 'orden')
    list_editable = ('nivel', 'orden')
    list_filter = ('categoria',)
    search_fields = ('nombre',)
    ordering = ('orden',)
