from utils.global_utils import id_generator
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter
)
from .serializers import (
    VideoCreateSerializer,
    VideoUpdateSerializer
)
from utils.models import videos


@extend_schema(tags=["Videos"])
@extend_schema_view()
class VideosViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    action_serializers = {
        "create": VideoCreateSerializer,
        "update": VideoUpdateSerializer
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super(VideosViewSet, self).get_serializer_class()

    @extend_schema(
        summary="Get all video records, with support for sorting",
        parameters=list([
            OpenApiParameter(
                name="sort_by",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                required=False,
                default="name",
            ),
            OpenApiParameter(
                name="order",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                required=False,
                default="asc",
            )
        ]),
    )
    def list(self, request):
        data = request.GET
        sort_by = data.get("sort_by")
        order = data.get("order", "asc")
        all_data = videos.all()

        if sort_by and sort_by in ["name", "post_date", "views_count"]:
            reverse = True if order.lower() == "desc" else False
            all_data = sorted(all_data, key=lambda x: x[sort_by], reverse=reverse)

        return Response(all_data)

    @extend_schema(summary="Add a new video record")
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

    @extend_schema(summary="Update an existing video record")
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

    @extend_schema(summary="Delete a video record by ID")
    def destroy(self, request, pk=None):
        video = videos.filter(lambda row: row["id"] == pk)
        if not video:
            return Response({"message": "Video not found!"}, 
                            status=status.HTTP_404_NOT_FOUND)

        videos.delete(lambda row: row["id"] == pk)
        return Response({"message": "Video was deleted successfully!"}, 
                        status=status.HTTP_200_OK)
