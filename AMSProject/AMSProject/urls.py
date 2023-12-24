"""AMSProject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
#Adding Sitemap to our Project
from django.contrib.sitemaps.views import sitemap
from newsApp.sitemaps import ArticleSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#STYLE THE LANDING PAGE OF THE ADMIN
admin.site.site_header = "NUST | AMS"
admin.site.site_title = "NUST AMS ADMIN"
admin.site.index_title = "WELCOME TO THE NUST ALUMNI NETWORK MANAGEMENT SYSTEM"


sitemaps = {
    'articles':ArticleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('landingApp.urls'), name="landing_page"),
    path('news/',include('newsApp.urls', namespace='newsApp')),
    path('gallery/',include('galleryApp.urls', namespace="galleryApp")),
    path('events/',include('eventsApp.urls', namespace='eventsApp')),
    path('vote/',include('votingApp.urls',namespace='votingApp')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('career-advice/',include('careerAdviceApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Auto_Create a url for the image

urlpatterns += staticfiles_urlpatterns()
