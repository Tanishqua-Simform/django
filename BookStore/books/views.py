from django.shortcuts import render
from rest_framework  import viewsets
from rest_framework.views  import APIView
from rest_framework.response  import Response
from rest_framework  import status
from .models import BookModel
from django.contrib.auth.models import User
from .serializers import BookSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import mixins, generics
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Function Based Views
## Method - 1 : Django like FBVs
@csrf_exempt
def custom_create_book(request):
    if request.method == "GET":
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def custom_update_book(request, pk):
    try:
        book = BookModel.objects.get(id=pk)
    except BookModel.DoesNotExist:
        raise Exception('Book Does not exist')

    if request.method == "GET":
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        book.delete()
        return JsonResponse({'status':'success', 'message':'Book Deleted Successfully!'}, status=status.HTTP_200_OK)
            

## Method - 2 : Using api_view decorator
@api_view(['GET', 'POST'])
def custom_create_book_decorator(request):
    if request.method == "GET":
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def custom_update_book_decorator(request, pk):
    try:
        book = BookModel.objects.get(id=pk)
    except BookModel.DoesNotExist:
        raise Exception('Book Does not Exist')

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        return Response({'status': 'success', 'message':'Book Deleted Successfully!'}, status=status.HTTP_200_OK)

# Class Based Views
## Method - 1 : Using ViewSets
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

## Method - 2 : Using APIView
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

class CustomBookUpdateView(APIView):
    def get_book_object(self, pk):
        try:
            return BookModel.objects.get(id=pk)
        except BookModel.DoesNotExist:
            # return Response({'status':'error', 'message':'Book Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
            # raise Exception('Book Does not exist')
            raise Http404

    def get(self, request, pk):
        book = self.get_book_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = self.get_book_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'status':'error', 'message':'Entered Data is not valid!'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        book = self.get_book_object(pk)
        book.delete()
        return Response({'status':'success', 'message':'Book Deleted Successfully!'})

## Method - 3 : Using Mixins
class CustomBookCreateViewMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class CustomBookUpdateViewMixin(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

## Method - 4 : Using Generics
class CustomBookCreateViewGeneric(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class CustomBookUpdateViewGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


## API Endpoints for User Model
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
