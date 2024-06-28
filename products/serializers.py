from rest_framework import serializers


class ProductSearchSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)


class ProductOutputSerializer(serializers.Serializer):
    image = serializers.URLField(required=True)