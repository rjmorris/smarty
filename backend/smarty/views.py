from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from .models import Drive
from .models import Attribute
from .models import Value
from .serializers import DriveSerializer
from .serializers import AttributeSerializer
from .serializers import ValueSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the smarty index.")


class DriveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drives to be viewed or edited.
    """
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows attributes to be viewed or edited.
    """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ValueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows values to be viewed or edited.
    """
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
