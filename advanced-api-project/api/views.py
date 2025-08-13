from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import BookSerializer , AuthorSerializer
from .models import Book ,Author
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticated  
# Create your views here.




class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Authorviewset(viewsets.ModelViewSet):
    queryset =Author.objects.all()
    serializer_class =AuthorSerializer    





class ListView (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
     
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]




class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
      

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    