from rest_framework import serializers

from library.serializers import LibrarySerializer
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    libraries = LibrarySerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
