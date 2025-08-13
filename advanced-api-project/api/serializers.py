from rest_framework import serializers
from .models import Book ,Author
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):  # convert book model to json
    class Meta:
        model = Book
        fields= '__all__'
    def validate_publication_year(self , value): # name must match the name you need to vaildate 
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future')
        return value




class AuthorSerializer(serializers.ModelSerializer):                         # convert author model to json
    books = BookSerializer(many=True , read_only = True)                     # -- nested serializer to get all books of author
    class Meta:
        model =Author
        fields = ['name' , 'books']


