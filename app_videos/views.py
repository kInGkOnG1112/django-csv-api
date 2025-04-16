from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter
)

# Create your views here.
@extend_schema(tags=['Videos'])
@extend_schema_view()
class VideosViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    @extend_schema(
        auth=[],
        responses=None,
        summary='Get the list of videos',
    )
    def list(self, request):
        return Response({})

    @extend_schema(
        auth=[],
        responses=None,
        summary='Create new video',
    )
    def create(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    @extend_schema(
        auth=[],
        responses=None,
        summary='Update existing video',
    )
    def update(self, request, pk=None):
        return Response({})

    @extend_schema(
        auth=[],
        responses=None,
        summary='Remove existing video',
    )
    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)