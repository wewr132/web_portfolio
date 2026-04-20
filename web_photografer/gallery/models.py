from django.db import models

class Category(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL-имя', max_length=100, unique=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField('Название фото', max_length=100)
    img = models.ImageField("Фотография", upload_to='portfolio_photos/')
    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE,
        related_name='photos',
        verbose_name='Категория'
    )

    upload_date = models.DateTimeField('Дата загрузки', auto_now_add=True)

    def __str__(self):
        return self.title


class SiteInfo(models.Model):
    class Meta:
        verbose_name = 'Настройки сайта'

    slogan = models.CharField('Слоган', max_length=255)
    slogan_bg = models.ImageField('Фон слогана', upload_to='site/', blank=True, null=True)
    about_text = models.TextField('Обо мне')
    about_photo = models.ImageField('Фото фотографа', upload_to='site/')
    vk = models.URLField('ВКонтакте', blank=True)
    tg = models.URLField('Telegram', blank=True)
    inst = models.URLField('Instagram', blank=True)
    email = models.EmailField('Email', blank=True)

    def __str__(self):
        return 'Глобальные настройки'