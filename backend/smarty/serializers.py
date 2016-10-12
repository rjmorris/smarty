from rest_framework import serializers
from .models import Drive, Attribute, Value


class DriveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drive
        fields = (
            'device_path',
            'user_label',
            'manufacturer',
            'model',
            'terabytes',
            'install_date'
        )


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = (
            'number',
            'label'
        )


class ValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Value
        fields = (
            'drive',
            'attribute',
            'date',
            'value'
        )
