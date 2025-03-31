from django.shortcuts import render
from rest_framework  import viewsets
from rest_framework.views  import APIView
from rest_framework.response  import Response
from rest_framework  import status
from .models import BookModel
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CustomBookCreateView(APIView):
    def get(self, request, *args, **kwargs):
        books = BookModel.objects.all()
        seralizer = BookSerializer(books, many=True)
        return Response(seralizer.data)

    def post(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        price = request.data.get('price')
        published_date = request.data.get('published_date')

        if not title or not author:
            return Response({
                'error': 'Title and Author are required fields.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        book = BookModel.objects.create(
            title=title,
            author=author,
            price=price,
            published_date=published_date
        )

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)