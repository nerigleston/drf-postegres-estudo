from rest_framework import serializers
from library.models import FileModel, Library


class LibrarySerializer(serializers.ModelSerializer):
    available_books = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = '__all__'

    def get_available_books(self, obj):
        available_books = obj.available_books()
        return [book.title for book in available_books]


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['files']
