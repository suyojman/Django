from django.urls import path, include
from . import views

urlpatterns = [
    path("book/", views.book_list, name="book_list"),
    path("book/create/", views.book_create, name="book_create"),
    path("book/edit/", views.book_edit, name="book_edit"),
    path("book/delete/", views.book_delete, name="book_delete"),
]
