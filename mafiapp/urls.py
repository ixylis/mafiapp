"""mafiapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include#, path
from django.conf import settings
from django.conf.urls.static import static

#from adminplus.sites import AdminSitePlus

#Add this line.  
#admin.site = AdminSitePlus()

admin.autodiscover()

urlpatterns = [
    #path('structure/', include('structure.urls')),
    #path('admin/', admin.site.urls),
    url(r'^abstract/', include('abstract.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^player/', include('playerinterface.urls')),
    url(r'^gm/', include('gminterface.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)