from django.contrib import admin
from .models import (
    DatosPersonales, ExperienciaLaboral, Reconocimiento, 
    CursoRealizado, ProductoAcademico, ProductoLaboral, VentaGarage,
    Documento
)


@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'numerocedula', 'sexo', 'perfilactivo')
    search_fields = ('nombres', 'apellidos', 'numerocedula', 'email')
    list_filter = ('sexo', 'perfilactivo', 'estadocivil')
    readonly_fields = ('idperfil',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('idperfil', 'descripcionperfil', 'perfilactivo', 'nombres', 'apellidos')
        }),
        ('Datos Personales', {
            'fields': ('nacionalidad', 'lugarnacimiento', 'fechanacimiento', 'numerocedula', 'sexo', 'estadocivil', 'licenciaconducir')
        }),
        ('Contacto', {
            'fields': ('telefonoconvencional', 'telefonofijo', 'direcciontrabajo', 'direcciondomiciliaria')
        }),
        ('Web y Multimedia', {
            'fields': ('sitioweb', 'foto_perfil')
        }),
    )


@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = ('cargodesempenado', 'nombrempresa', 'fechainiciogestion', 'fechafingestion', 'activarparaqueseveaenfront')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('cargodesempenado', 'nombrempresa', 'emailempresa')
    list_filter = ('fechainiciogestion', 'activarparaqueseveaenfront')
    readonly_fields = ('idexperiencialaboral',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('idexperiencialaboral', 'idperfilconqueestaactivo', 'cargodesempenado', 'nombrempresa', 'lugarempresa')
        }),
        ('Empresa', {
            'fields': ('emailempresa', 'sitiowebempresa', 'nombrecontactoempresarial', 'telefonocontactoempresarial')
        }),
        ('Fechas y Descripción', {
            'fields': ('fechainiciogestion', 'fechafingestion', 'descripcionfunciones', 'imagen')
        }),
        ('Visibilidad y Certificado', {
            'fields': ('activarparaqueseveaenfront', 'rutacertificado', 'certificado_archivo')
        }),
    )


@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('tituloreconocimiento', 'tiporeconocimiento', 'entidadpatrocinadora', 'fechareconocimiento', 'activarparaqueseveaenfront')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('tituloreconocimiento', 'descripcionreconocimiento', 'entidadpatrocinadora')
    list_filter = ('tiporeconocimiento', 'fechareconocimiento', 'activarparaqueseveaenfront')
    readonly_fields = ('idreconocimiento',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('idreconocimiento', 'idperfilconqueestaactivo', 'tituloreconocimiento', 'tiporeconocimiento', 'fechareconocimiento')
        }),
        ('Descripción', {
            'fields': ('descripcionreconocimiento', 'entidadpatrocinadora')
        }),
        ('Contacto', {
            'fields': ('nombrecontactoauspicia', 'telefonocontactoauspicia')
        }),
        ('Visibilidad y Certificado', {
            'fields': ('activarparaqueseveaenfront', 'rutacertificado', 'certificado_archivo')
        }),
    )


@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = ('nombrecurso', 'entidadpatrocinadora', 'fechainicio', 'totalhoras', 'activarparaqueseveaenfront')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombrecurso', 'entidadpatrocinadora')
    list_filter = ('fechainicio', 'activarparaqueseveaenfront')
    readonly_fields = ('idcursorealizado',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('idcursorealizado', 'idperfilconqueestaactivo', 'nombrecurso', 'descripcioncurso')
        }),
        ('Fechas y Duración', {
            'fields': ('fechainicio', 'fechafin', 'totalhoras')
        }),
        ('Entidad Patrocinadora', {
            'fields': ('entidadpatrocinadora', 'nombrecontactoauspicia', 'telefonocontactoauspicia', 'emailempresapatrocinadora')
        }),
        ('Visibilidad y Certificado', {
            'fields': ('activarparaqueseveaenfront', 'rutacertificado', 'certificado_archivo')
        }),
    )


@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'clasificador', 'activarparaqueseveaenfront')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombrerecurso', 'descripcion')
    list_filter = ('activarparaqueseveaenfront',)
    readonly_fields = ('idproductoacademico',)


@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'fechaproducto', 'activarparaqueseveaenfront')
    list_editable = ('activarparaqueseveaenfront',)
    search_fields = ('nombreproducto', 'descripcion')
    list_filter = ('fechaproducto', 'activarparaqueseveaenfront')
    readonly_fields = ('idproductoslaborales',)


@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'estadoproducto', 'valordelbien', 'activarparaqueseveaenfront')
    list_editable = ('estadoproducto', 'activarparaqueseveaenfront')
    search_fields = ('nombreproducto',)
    list_filter = ('estadoproducto', 'activarparaqueseveaenfront')
    readonly_fields = ('idventagarage',)


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'idperfilconqueestaactivo', 'activarparaqueseveaenfront', 'orden')
    list_editable = ('activarparaqueseveaenfront', 'orden')
    search_fields = ('titulo', 'contenido')
    list_filter = ('activarparaqueseveaenfront',)
    readonly_fields = ('iddocumento',)
    fieldsets = (
        ('Información', {
            'fields': ('iddocumento', 'idperfilconqueestaactivo', 'titulo', 'slug')
        }),
        ('Contenido', {
            'fields': ('contenido',)
        }),
        ('Visibilidad', {
            'fields': ('activarparaqueseveaenfront', 'orden')
        }),
    )

