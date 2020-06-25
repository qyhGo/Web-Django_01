"""django_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app_01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^layout/', views.layout),
    url(r'^teacher/',views.teacher),
    url(r'^class/', views.manage),
    url(r'^classes/', views.classes),
    url(r'^add_class/', views.add_class),
    url(r'^del_class/', views.del_class),
    url(r'^edit_class/', views.edit_class),
    url(r'^add_teacher/', views.add_teacher),
    url(r'^del_teacher/', views.del_teacher),
    url(r'^edit_teacher/', views.edit_teacher),
    url(r'^student/', views.student),
    url(r'^add_student/', views.add_student),
    url(r'^edit_student/', views.edit_student),
    url(r'^modal_add_class/',views.modal_add_class),
    url(r'^modal_edit_class/',views.modal_edit_class),
    url(r'^modal_del_class/',views.modal_del_class),
    url(r'^modal_add_student/',views.modal_add_student),
    url(r'^modal_add_teacher/',views.modal_add_teacher),
    url(r'^modal_edit_student/',views.modal_edit_student),
    url(r'^modal_del_student/',views.modal_del_student),
    url(r'^get_class_list/',views.get_class_list),
]
