from rest_framework import serializers

from .models import Menus

class MenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Menus
        fields = ('title','ingredients','cook_time','created_at')