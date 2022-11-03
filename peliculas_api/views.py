from .models import Movie, Reaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer, ReactionSerializer


@api_view(['POST'])
def movies_create(request):
    serializar = MovieSerializer(data=request.data)
    if serializar.is_valid():
        serializar.save()
    return Response(serializar.data)


@api_view(['GET'])
def movies_read(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movies_read_details(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def movies_update(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializar = MovieSerializer(instance=movie, data=request.data)
    if serializar.is_valid():
        serializar.save()
    return Response(serializar.data)


@api_view(['DELETE'])
def movies_delete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return Response("Movie Deleted")


@api_view(['POST'])
def reaction_create(request):
    serializar = ReactionSerializer(data=request.data)
    if serializar.is_valid():
        serializar.save()
    return Response(serializar.data)


@api_view(['GET'])
def reaction_read(request):
    reaction = Reaction.objects.all()
    serializer = ReactionSerializer(reaction, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def reaction_update(request, pk):
    try:
        reaction = Reaction.objects.get(id=pk)
    except Reaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializar = ReactionSerializer(instance=reaction, data=request.data)
    if serializar.is_valid():
        serializar.save()
    return Response(serializar.data)


@api_view(['DELETE'])
def reaction_delete(request, pk):
    reaction = Reaction.objects.get(id=pk)
    reaction.delete()
    return Response("Reaction Delete")
