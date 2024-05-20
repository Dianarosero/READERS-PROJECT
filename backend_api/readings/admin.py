from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Mostrar todos los campos del modelo
    list_display = [field.name for field in Book._meta.fields]

# Registrar el modelo utilizando la clase personalizada BookAdmin
admin.site.register(Book, BookAdmin)
