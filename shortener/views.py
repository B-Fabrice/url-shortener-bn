from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from shortener.serializers import LinkSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shorten(request):
    serializer = LinkSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        link = serializer.save()
        return Response(LinkSerializer(link).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def urls(request):
    user = request.user
    links = user.links.all().order_by('-created_at')
    serializer = LinkSerializer(links, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
