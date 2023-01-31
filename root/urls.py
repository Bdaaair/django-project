"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from coded.views import get_home, createevents, get_event, myprofile, nono,editevent,deletevent
from users.views import user_login, user_register, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', get_home, name="home"),
    path('login/', user_login, name="login"),
    path('logout/', logout_view, name="logout"),
    path('createevent/', createevents, name="createevent"),
    path('register/', user_register, name="register"),
    path('event/<int:obj_id>/', get_event, name="event"),
    path('myprofile/', createevents, name="myprofile"),

    path('edit/<int:id>', editevent, name="edit"),
    path('delete/<int:id>', deletevent, name="delete"),
    path('nono/', nono, name="nono"),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
