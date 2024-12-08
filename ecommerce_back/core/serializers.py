from rest_framework import serializers
from .models import Item
from bson import ObjectId


class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)  # Convert ObjectId to string for JSON

    def to_internal_value(self, data):
        if ObjectId.is_valid(data):
            return ObjectId(data)
        raise serializers.ValidationError("Invalid ObjectId")

class ProductListSerializer(serializers.ModelSerializer):
    id = ObjectIdField()
    class Meta:
        model = Item
        fields = "__all__"
    def create(self, validated_data):
        # Handle the 'id' field specifically if necessary
        # For example, generate an ObjectId or handle it differently
        if 'id' not in validated_data:
            validated_data['id'] = str(ObjectId())  # Generate an ObjectId if it's missing
        
        # Now create the instance with the validated data
        return Item.objects.create(**validated_data)
