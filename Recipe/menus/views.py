
from rest_framework import viewsets

from .serializers import MenusSerializer
from .models import Menus

# Create your views here.

class MenusViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all().order_by('title')
    serializer_class = MenusSerializer 