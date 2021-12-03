from django.urls import path

from . import views
app_name='todoList'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('list', views.list, name='list'),
    path('submit', views.submit, name='submit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]