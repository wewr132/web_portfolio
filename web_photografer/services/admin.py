from django.contrib import admin
from .models import Order, Review


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service_type', 'date', 'status', 'user_email')

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email пользователя'


admin.site.register(Order, OrderAdmin)
admin.site.register(Review)
