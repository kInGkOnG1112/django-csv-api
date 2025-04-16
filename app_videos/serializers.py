from rest_framework import serializers
from utils.global_utils import is_valid_date

optional = {
    "default": '',
    "allow_blank": True,
    "allow_null": True
}


class VideoSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=2000)
    href = serializers.CharField(max_length=3000)
    post_date = serializers.CharField(max_length=50)
    views_count = serializers.IntegerField()

    class Meta:
        fields = "__all__"

    def validate(self, attrs):
        errors = dict()
        post_date = attrs.get("post_date")

        if not is_valid_date(post_date):
            errors["post_date"] = "Invalid date format! It should be MM/DD/YYYY."

        if errors:
            raise serializers.ValidationError(errors)
        return attrs
