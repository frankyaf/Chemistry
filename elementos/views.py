from rest_framework import viewsets
from .models import Elemento
from .serializers import ElementoSerializer
from .serializers import ShortElementoSerializer

class ElementoViewSet(viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer

class ShortElementoViewSet(viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ShortElementoSerializer