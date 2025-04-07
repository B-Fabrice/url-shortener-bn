from rest_framework import serializers
from shortener.models import Link

class LinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()
    class Meta:
        model = Link
        fields = ['id', 'original_url', 'key', 'user', 'created_at', 'short_url']
        read_only_fields = ['id', 'key', 'user', 'created_at', 'short_url']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
    
    def get_short_url(self, obj):
        request = self.context.get('request')
        if request:
            base_url = request.build_absolute_uri('/')
            return f"{base_url}{obj.key}"
        else:
            return obj.original_url