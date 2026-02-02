from django.db import models


class Perfil(models.Model):
    nombre = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.nombre


class Educacion(models.Model):
    titulo = models.CharField(max_length=200)
    centro = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    anio_inicio = models.IntegerField()
    anio_fin = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Educación"
        verbose_name_plural = "Educación"
        ordering = ['-anio_fin', '-anio_inicio', 'orden']

    def __str__(self):
        return f"{self.titulo} - {self.centro}"


class Experiencia(models.Model):
    cargo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    en_curso = models.BooleanField(default=False)
    orden = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencia"
        ordering = ['-fecha_fin', '-fecha_inicio', 'orden']

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"


class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField(
        default=50,
        help_text="Nivel de 0 a 100"
    )
    categoria = models.CharField(
        max_length=50,
        default="Técnica",
        choices=[
            ('Técnica', 'Técnica'),
            ('Blanda', 'Blanda'),
            ('Idioma', 'Idioma'),
            ('Otra', 'Otra'),
        ]
    )
    orden = models.IntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre
