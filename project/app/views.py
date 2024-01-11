from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer


class BooksView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def allBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('Success Created')


@api_view(['PATCH'])
def update(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(data=request.data, instance=book, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return Response('Success Deleted')