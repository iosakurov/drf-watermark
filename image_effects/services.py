from PIL import Image
import re
import io

WATERMARK_PATH = './wtmark.png'


def make_watermark_for_ImageFile(file, source_filename):
	"""
	Создает вотермарку и возвращает имя файла, формат
	для ImageFile поля модели

	"""
	watermarked_img = _make_watermark(file)
	image_bytes = io.BytesIO()
	watermarked_img.save(image_bytes, format='PNG')

	file_name, file_format = separate_image_name_and_format(source_filename)

	return image_bytes, file_name, file_format


def separate_image_name_and_format(image_name: str):
	"""
	Возвращает разделенное имя файла и его формат
	"""
	parse_result = re.split('\.(jpg|jpeg|png)$', image_name)
	if len(parse_result) == 1:
		raise AttributeError('Не верный формат', image_name)

	file_name, file_format = parse_result[0], parse_result[1]

	return file_name, file_format


def _make_watermark(source_img, watermark=WATERMARK_PATH, format_img='PNG'):
	watermark_source = Image.open(watermark).convert('RGBA')
	img = Image.open(source_img)
	watermark = watermark_source.resize(img.size)
	position = (int(img.width / 2 - watermark.width / 2),
				int(img.height / 2 - watermark.height / 2))

	new_image = Image.new('RGBA', (img.width, img.height), (0, 0, 0, 0))
	new_image.paste(img, (0, 0))
	new_image.paste(watermark, position, mask=watermark)
	new_image = new_image.convert('RGB')
	print('Watermark added.')
	return new_image
