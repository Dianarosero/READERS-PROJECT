from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre','published_year', 'isbn', 'publisher', 'pages', 'language'
                  , 'description', 'cover_image_url','created_at', 'updated_at', 'status']