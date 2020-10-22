from django.urls import path,include
from . import views

urlpatterns= [
   # url(r'^$', views.index, name='index')
   path('', views.applications_create, name='application_insert'),
   path('<int:id>/', views.applications_create, name='application_update'),
   path('delete/<int:id>/', views.applications_delete, name='application_delete'),
   path('list/', views.applications_list, name='application_list')
    
    ]
 