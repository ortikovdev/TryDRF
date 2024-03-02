from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer, ArticlePostSerializer


@api_view(['GET'])
def article_list(request):
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, pk):
    obj = get_object_or_404(Article, id=pk)
    serializer = ArticleSerializer(obj)
    return Response(serializer.data)


@api_view(['POST'])
def article_create(request):
    context = {
        'user_id': request.user.id
    }
    serializer = ArticleSerializer(data=request.data, context=context)
    if serializer.is_valid():
        serializer.save()
        obj = get_object_or_404(Article, id=serializer.data.get('id'))
        success_serializer = ArticleSerializer(obj)
        return Response(success_serializer.data, status=status.HTTP_201_CREATED)
    data = {
        'errors': serializer.errors,
        'message': "Something went wrong",
    }
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated]) # log in qilingan bo'lsa permission beradi, aks holda yo'q
# @authentication_classes([BasicAuthentication])
def list_create_view(request):
    if request.method == "POST":
        serializer = ArticlePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            obj = get_object_or_404(Article, id=serializer.data.get('id'))
            success_serializer = ArticleSerializer(obj)
            return Response(success_serializer.data, status=status.HTTP_201_CREATED)
        data = {
            'errors': serializer.errors,
            'message': "Something went wrong",
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)

