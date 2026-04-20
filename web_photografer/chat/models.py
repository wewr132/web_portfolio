from django.db import models
from django.conf import settings
 
class ChatMessage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete= models.CASCADE,
        related_name='message', 
        verbose_name= 'Автор'
    )

    text = models.TextField('Текст отзыва')
    created_at = models.DateTimeField('Время отправки', auto_now_add=True)
    is_deleted = models.BooleanField('Удалено', default = False)

    def __str__(self):
        return f'{self.user.username} ({self.created_at.strftime('%Y-%m-%d %H:%M')}): {self.text[:20]}...'