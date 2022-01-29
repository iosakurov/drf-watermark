from rest_framework import serializers
from .models import Images


class UploadImageSerializer(serializers.Serializer):
	source_img = serializers.ImageField(allow_empty_file=False)


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Images
		fields = '__all__'
