from django.db import models
from django.conf import settings

class Order(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'Новый'
        IN_PROGRESS = 'IN_PROGRESS', 'В работе'
        COMPOLETED = 'COMPOLETED', 'Завершен'

    class ServiceType(models.TextChoices):
        NATURE = 'NATURE', 'Природа'
        STUDIO = 'STUDIO', 'Студия'
        PORTRAITS = 'PORTRAITS', 'Портреты'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name= 'Пользователь'
    )
    service_type = models.CharField('Тип услуги', max_length=20, choices=ServiceType.choices)
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=20, choices = Status.choices, default = Status.NEW)
    contact_info = models.CharField('Контактная информация', max_length=255)
    
    def __str__(self):
        return f'Заказ #{self.id} от {self.user.username}'
    
class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='review', 
        verbose_name= 'Пользователь'
    )
    text = models.TextField('Текст отзыва')
    reting = models.PositiveSmallIntegerField(
        'Оценка',
        choices = [(1, '1'), (2, '2'), (3,'3'), (4,'4'),(5,'5')]
    )
    is_published = models.BooleanField('Опубликовано', default=False)
    
    def __str__(self):
        return f'Отзвы от {self.user.username}'