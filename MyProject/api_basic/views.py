from django.shortcuts import render
from django.http import  HttpResponse,JsonResponse
from .models import Artical
from .serializer import ArticalSerializer
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        if id:
            return self.retrieve(id)
        else:
            return self.list(request)

    def post(self, request):
        return  self.create(request)

    def put(self,request , id = None):
        return self.update(request,id)

    def delete(self, request, id):
        return self.destroy(request, id)


class ArticleAPIView(APIView):
    def get(self,request):
        artical = Artical.objects.all()
        serializers = ArticalSerializer(artical, many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers = ArticalSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self, pk):
        try:
            return Artical.objects.get(pk=pk)

        except Artical.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        artical = self.get_object(id)
        serializers = ArticalSerializer(artical)
        return Response(serializers.data)

    def put(self,request,id):
        artical = self.get_object(id)
        serializers = ArticalSerializer(artical, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        artical = self.get_object(id)
        artical.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
