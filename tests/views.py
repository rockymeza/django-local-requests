from rest_framework import (
    serializers,
    viewsets,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            'url',
            'author',
            'title',
        )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = (
            'url',
            'name',
            'books',
        )


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


@api_view(['GET', 'POST'])
def echo(request):
    return Response({
        'GET': request.GET,
        'POST': request.POST,
        'META': request.META,
    })


@api_view(['POST'])
def upload_file(request):
    file = request.FILES['file']
    return Response({
        'name': file.name,
        'content': file.read().decode('utf-8'),
    })
