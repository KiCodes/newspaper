from django.contrib import admin
from .models import User, New, Category, Blog, Message

# Register your models here.
admin.site.register(User)
admin.site.register(New)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Message)
