from utils.global_utils import id_generator
from .serializers import VideoSerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view
)
from utils.models import videos


@extend_schema(tags=["Videos"])
@extend_schema_view()
class VideosViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    action_serializers = {
        "create": VideoSerializer,
        "update": VideoSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super(VideosViewSet, self).get_serializer_class()

    @extend_schema(summary="Get the list of videos")
    def list(self, request):
        all_data = videos.all()
        return Response(all_data)

    @extend_schema(summary="Create new video")
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = serializer.data
        while True:
            row_id = id_generator()
            if not videos.filter(lambda row: row["id"] == row_id):
                break

        record = {"id": str(row_id), **data}
        videos.add(record)
        return Response({"message": "Video was successfully created!"}, 
                        status=status.HTTP_201_CREATED)

    @extend_schema(summary="Update existing video")
    def update(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        video = videos.filter(lambda row: row["id"] == pk)
        if not video:
            return Response({"message": "Video not found!"}, 
                            status=status.HTTP_404_NOT_FOUND)

        data = serializer.data
        videos.update(lambda row: row["id"] == pk, data)
        return Response({"message": "Video was successfully updated!"}, 
                        status=status.HTTP_200_OK)

    @extend_schema(summary="Remove existing video")
    def destroy(self, request, pk=None):
        video = videos.filter(lambda row: row["id"] == pk)
        if not video:
            return Response({"message": "Video not found!"}, 
                            status=status.HTTP_404_NOT_FOUND)

        videos.delete(lambda row: row["id"] == pk)
        return Response({"message": "Video was deleted successfully!"}, 
                        status=status.HTTP_200_OK)
