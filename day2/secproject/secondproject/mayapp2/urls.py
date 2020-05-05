from django.urls import path
from mayapp2 import views
urlpatterns = [
    path('',views.hello,name='hello'),
    path('register/',views.register,name='register'),
    path('reports/',views.reports,name="reports"),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    ]