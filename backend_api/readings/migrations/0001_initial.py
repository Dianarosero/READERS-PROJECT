# Generated by Django 5.0.6 on 2024-05-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(help_text='Identificador único y autoincremental para cada libro', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Título del libro', max_length=255)),
                ('author', models.CharField(help_text='Autor del libro', max_length=255)),
                ('genre', models.CharField(help_text='Género del libro', max_length=100)),
                ('published_year', models.IntegerField(help_text='Año de publicación del libro')),
                ('isbn', models.CharField(help_text='Número Internacional Normalizado del Libro (ISBN)', max_length=13)),
                ('publisher', models.CharField(help_text='Editorial que publicó el libro', max_length=255)),
                ('pages', models.IntegerField(help_text='Número de páginas del libro')),
                ('language', models.CharField(help_text='Idioma en el que está escrito el libro', max_length=50)),
                ('description', models.TextField(help_text='Descripción del libro')),
                ('cover_image_url', models.CharField(help_text='URL de la imagen de portada del libro', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se creó el registro, con un valor predeterminado de la marca de tiempo actual')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se actualizó el registro por última vez, con actualización automática')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Fecha y hora en que se eliminó el registro (permite valores nulos)', null=True)),
                ('status', models.BooleanField(default=True, help_text='Estado del libro, con un valor predeterminado de "true" (indica que el libro está activo)')),
            ],
        ),
    ]
