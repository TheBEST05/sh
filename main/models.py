from django.db import models


class Product(models.Model):
	title = models.CharField('Название', max_length=100)
	description = models.TextField('Описание', max_length=3000)
	price = models.IntegerField('Цена')
	img = models.ImageField('Картинка', upload_to='products', blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

