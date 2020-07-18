from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:category>", views.category, name="category"),
    path("new/<str:new>", views.new, name="new"),
    path("blog/<int:id>", views.blog, name="blog"),
    path("allnews", views.allnews, name="allnews"),
    path("allblogs", views.allblogs, name="allblogs"),
    path("contact", views.contact, name="contact"),
]