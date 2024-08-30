from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer
from account.authenticate import CustomAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def create_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_persons(request):
    objects = Person.objects.all()
    serializer = PersonSerializer(objects, many=True)
    return Response(serializer.data,status=200)


@api_view(['GET'])
def retrieve_persons(request,pk):
    obj = get_object_or_404(Person,id=pk)
    serializer = PersonSerializer(obj)
    return Response(serializer.data,status=200)


@api_view(['PUT','PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def update_person(request, pk):
    obj = get_object_or_404(Person,id=pk)
    serializer = PersonSerializer(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([CustomAuthentication])
def delete_person(request, pk):
    obj = get_object_or_404(Person,id=pk)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)









