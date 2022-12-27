from django.contrib import admin

# Register your models here.
from news_2105010240.models import *
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Best)
admin.site.register(UserProfile)
admin.site.register(Comment)
