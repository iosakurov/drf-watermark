from PIL import Image
import io
import re

from django.core.files.images import ImageFile
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

from .serializers import UploadImageSerializer, ImageSerializer
from .models import Profile, Images
from .services import make_watermark_for_ImageFile


class ImageAddWatermark(CreateAPIView):
	queryset = Profile.objects.all()
	serializer_class = UploadImageSerializer

	def post(self, request, *args, **kwargs):
		image = request.data['source_img']
		image_source_name = request.data['source_img'].name

		image_bytes, file_name, file_format = make_watermark_for_ImageFile(image, image_source_name)
		image_watermarked = ImageFile(image_bytes, name=f'{file_name}.{file_format}')

		profile = Profile.objects.get(user=request.user)
		img = Images.objects.create(profile=profile, image=image, image_watermarked=image_watermarked)
		img.save()
		return redirect(reverse('get-image-info', kwargs={'pk': img.pk}))


class ImageView(RetrieveAPIView):
	queryset = Images.objects.all()
	serializer_class = ImageSerializer
