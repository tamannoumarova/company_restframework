from rest_framework import serializers
from profession.models import Profession

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class ProfessionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"