"""
URL configuration for supermarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#      path('', views.index, name='index'),
# ]




from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   # url for index.html page
    path('signup', views.signup, name='signup'),   # url for signup.html page
    path('signin', views.signin, name='signin'),   # url for signin.html page
    path('homepage', views.homepage, name='homepage'), # url for signin.html page
    path('delete', views.delete, name='delete'),  # url for signin.html page
    path('update', views.update, name='update'),  # url for signin.html page

    path('create_user', views.create_user, name='create-user'),  # to point out the create_user method
    path('signin_user', views.signin_user, name='signin-user'),  # to point out the signin_user method
    path('delete_user', views.delete_user, name='delete-user'),  # to point out the delete_user method
     path('update_user', views.update_user, name='update-user'), # to point out the upadate_user method
]
