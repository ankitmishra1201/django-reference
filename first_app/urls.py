from django.urls import path
from first_app import views
from django.conf.urls import include

urlpatterns=[
    path('',views.index,name='index'),
    path('formpage/',views.form_name_view,name='form_name'),
]