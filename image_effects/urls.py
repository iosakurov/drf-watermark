from django.urls import path
from .views import ImageAddWatermark, ImageView

# app_name = 'image_effects'
urlpatterns = [
	path('image/add-watermark', ImageAddWatermark.as_view()),
	path('image/<int:pk>', ImageView.as_view(), name='get-image-info'),
]
