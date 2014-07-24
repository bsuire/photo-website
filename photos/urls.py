from django.conf.urls import url

from photos import views

urlpatterns = [
            url(r'^$', views.home, name='home'),
            url(r'^aboutme/$', views.aboutme, name='aboutme'),
            url(r'^(?P<album_name>\w+)/$', views.gallery, name='gallery'),
            
            ]
