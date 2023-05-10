from rest_framework import serializers

from .models import Menus

class MenusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Menus
        fields = ('title','description','ingredients','instrutions','perp_time','cook_time','created_at')