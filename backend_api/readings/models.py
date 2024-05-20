from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True, help_text='Identificador único y autoincremental para cada libro')
    title = models.CharField(max_length=255, help_text='Título del libro')
    author = models.CharField(max_length=255, help_text='Autor del libro')
    genre = models.CharField(max_length=100, help_text='Género del libro')
    published_year = models.IntegerField(help_text='Año de publicación del libro')
    isbn = models.CharField(max_length=13, help_text='Número Internacional Normalizado del Libro (ISBN)')
    publisher = models.CharField(max_length=255, help_text='Editorial que publicó el libro')
    pages = models.IntegerField(help_text='Número de páginas del libro')
    language = models.CharField(max_length=50, help_text='Idioma en el que está escrito el libro')
    description = models.TextField(help_text='Descripción del libro')
    cover_image_url = models.CharField(max_length=255, help_text='URL de la imagen de portada del libro')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creó el registro, con un valor predeterminado de la marca de tiempo actual')
    updated_at = models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se actualizó el registro por última vez, con actualización automática')
    deleted_at = models.DateTimeField(null=True, blank=True, help_text='Fecha y hora en que se eliminó el registro (permite valores nulos)')
    status = models.BooleanField(default=True, help_text='Estado del libro, con un valor predeterminado de "true" (indica que el libro está activo)')

    def __str__(self):
        return self.title
