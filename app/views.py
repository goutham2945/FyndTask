# Django imports
from django.core.exceptions import ObjectDoesNotExist

# 3rd party imports
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

# Custom imports
from app.serializers import MovieSerializer, GenreSerializer 
from app.models import Movie,Genre

class Movies(APIView):

    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = (permissions.IsAdminUser,)

    def get(self,request):
        movies = Movie.objects.all()
        data = MovieSerializer(movies,many=True).data
        return Response(data, status=status.HTTP_200_OK)

    parser_classes = (JSONParser,)

    def post(self,request):
        data = request.data
        
        if not len(data["genre"]):
           return Response(status=status.HTTP_404_NOT_FOUND)

        for genre in data["genre"]:
            Genre.objects.get_or_create(name=genre.strip())

        serializer  = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieData(APIView):

    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = (permissions.IsAdminUser,)
   
    def get(self, request, _id):
        try:
            movie = Movie.objects.get(pk=_id)
            data = MovieSerializer(movie).data
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, _id):
        try:
            movie = Movie.objects.get(pk=_id)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, _id):
        try:
            movie = Movie.objects.get(pk=_id)
            data = request.data

            if not len(data["genre"]):
               return Response(status=status.HTTP_404_NOT_FOUND)

            for genre in data["genre"]:
               Genre.objects.get_or_create(name=genre.strip())

            serializer = MovieSerializer(movie, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

   
class SearchMovie(APIView):

    def get(self,request):
        queryset = Movie.objects.all()
        query = request.query_params

        name =  query.get('name',None)
        if name:
            queryset = queryset.filter(name__icontains=name)

        director = query.get('director',None)
        if director:
            queryset = queryset.filter(director__icontains=director)

        genre = query.get('genre',None)
        if genre:
           queryset= queryset.filter(genre__name__icontains=genre)

        data = MovieSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)
