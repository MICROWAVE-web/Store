from rest_framework import serializers

from .models import *


class PropertyValueSerializer(serializers.Serializer):
    property_type = serializers.CharField(source='property_type.title', max_length=1000)
    value = serializers.CharField(max_length=1000)

    class Meta:
        model = PropertyValue
        fields = ('value',)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=5000)
    created = serializers.DateTimeField()
    slug = serializers.SlugField(max_length=1200)
    parent = serializers.CharField(source='parent.title', max_length=1000)
    parent_slug = serializers.CharField(source='parent.slug', max_length=1000)


class ProductByIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=5000)
    created = serializers.DateTimeField()
    slug = serializers.SlugField(max_length=1200)
    parent = serializers.CharField(source='parent.title', max_length=1000)
    parent_slug = serializers.CharField(source='parent.slug', max_length=1000)
    properties = PropertyValueSerializer(many=True)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=5000)
    created = serializers.DateTimeField()
    slug = serializers.SlugField(max_length=1200)
    parent = serializers.CharField(source='parent.title', max_length=1000, default='None', allow_null=True)
    parent_slug = serializers.CharField(source='parent.slug', max_length=1000, default='None', allow_null=True)


class CategoryByIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=1000)
    description = serializers.CharField(max_length=5000)
    created = serializers.DateTimeField()
    slug = serializers.SlugField(max_length=1200)
    parent = serializers.CharField(source='parent.title', max_length=1000, default='None', allow_null=True)
    parent_slug = serializers.CharField(source='parent.slug', max_length=1000, default='None', allow_null=True)
    categories = CategorySerializer(many=True, default='None', allow_null=True)
    products = ProductByIdSerializer(many=True)
