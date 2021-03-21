from rest_framework.response import Response
from netflix.models import Movies
from .serializers import MovieSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes

class IsManager(BasePermission):
    def has_permission(Self, request, view):
        return request.user.has_perm("netflix.view_movie")

@api_view(["POST",])  
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception  as e:  
            return Response(data={
                "success":False,
                "errors":str(e)
           }, status=status.HTTP_400_BAD_REQUEST)
            
            
            return Response(data={
                "success": True,
                "message": "Movie has been created successfully"
        }, status=status.HTTP_201_CREATED)


    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST) 

    

@api_view(["GET",])
@permission_classes([IsAuthenticated, IsManager])
def index(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)



@api_view(["POST",])
def create(request, id):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success" : True,
            "message" : "Movie has been created Successfully"
        }, status=status.HTTP_201_CREATED)


#Else
     

class MovieList(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer



class CreateMovie(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class UpdateMovie(generics.UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class  MovieViewSet(viewsets.ModelViewSet):
    model = Movies
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]







