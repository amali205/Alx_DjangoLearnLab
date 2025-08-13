from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import BookSerializer , AuthorSerializer
from .models import Book ,Author
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters 
from django_filters.rest_framework import DjangoFilterBackend  
# Create your views here.




class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend , filters.SearchFilter , filters.OrderingFilter]
    
    # Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Searching
    search_fields = ['title', 'author']

    # Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering














class Authorviewset(viewsets.ModelViewSet):
    queryset =Author.objects.all()
    serializer_class =AuthorSerializer    
    permission_classes =[IsAuthenticatedOrReadOnly]




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
    