from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('new', views.new, name='new'),
    path('<int:id>/new_com',views.new_com, name='new_com'),
    path('create', views.create, name='create'),
    path('create_com',views.create_com,name='create_com'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
]
