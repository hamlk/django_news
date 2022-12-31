"""CMS_2105010240 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from news_2105010240.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', index, name='index'),
    url('addpage/', Addpage, name='Addpage'),
    url('category/(?P<cate_id>\d+)/$', category, name='category'),
    url('detail/(?P<article_id>\d+)/$', detail, name='detail'),
    url('deletepage/(?P<cate_id>\d+)/$', deletepage, name='deletepage'),
    url('login/', login, name='login'),
    url('register/', register, name='register'),
    url('logout/', logout, name='logout'),
    url('profile/', profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
