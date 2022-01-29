from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)



class Images(models.Model):
	def img_path(self, filename):
		return f'photos/{self.profile.user.username}/{filename}'

	def img_watermark_path(self, filename):
		return f'photos/{self.profile.user.username}/wt/{filename}'

	image = models.ImageField(upload_to=img_path, blank=True)
	image_watermarked = models.ImageField(upload_to=img_watermark_path, blank=True)
	profile = models.ForeignKey(Profile, related_name='images', on_delete=models.CASCADE)