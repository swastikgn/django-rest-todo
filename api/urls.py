from django.urls import path
from .views import *

urlpatterns = [
    path("create/",TodoCreate.as_view()),
    path("delete/<int:pk>",TodoDelete.as_view()),
    path("list/",TodoList.as_view()),
    path("update/<int:pk>",TodoUpdate.as_view()),



 

 ]