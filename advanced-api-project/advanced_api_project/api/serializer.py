from rest_framework import serializers
from .models import Book , Author
from datetime import date



class BookSerializer(serializers.ModelSerializer):
    class Meta:
     model = Book
     fields = '__all__'
    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
   books = BookSerializer(many = True)
   class Meta :
      model = Author
      fields = ['name']      