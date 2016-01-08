"""Jeevuthan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home import views as home_views
from register_for_pet import views as register_for_pet_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #user auth urls
    url(r'^accounts/login/$', register_for_pet_views.login),
    url(r'^accounts/auth/$', register_for_pet_views.auth_view),
    url(r'^accounts/logout/$', register_for_pet_views.logout),
    url(r'^accounts/loggedin/$', register_for_pet_views.loggedin),
    url(r'^accounts/invalid/$', register_for_pet_views.invalid_login),
    url(r'^registeruser/$', register_for_pet_views.registeruser),
    url(r'^accounts/register_success/$', register_for_pet_views.register_success),
    url(r'^registerpet/$', register_for_pet_views.registerpet,name='registerpet'),

    #app urls
    url(r'^$', home_views.homepage,name='homepage'),
    url(r'^aboutus/$',home_views.aboutus,name='aboutus'),
    url(r'^faqs/$',home_views.faqs,name='faqs'),
    url(r'^contactus/$',home_views.contactus,name='contactus'),
    url(r'^otheruser/$',home_views.otheruser,name='otheruser'),
    url(r'^location/$', home_views.location,name='location'),
    url(r'^registerngo/$', home_views.ngo,name='registerngo'),
    url(r'^registervet/$', home_views.vet,name='registervet'),

    url(r'^captcha/', include('captcha.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)