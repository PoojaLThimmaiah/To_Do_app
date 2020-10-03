from django.urls import path, include
from todo_app import views

app_name = "todo_app"

urlpatterns = [
    path("", views.home, name= "home"),
    path("about/", views.about, name= "about"),
    path("<int:pk>/remove/", views.remove, name= "remove"),
    path("<int:pk>/cross/", views.cross, name= "cross"),
    path("<int:pk>/uncross/", views.uncross, name= "uncross"),
    path("<int:pk>/edit/", views.edit, name= "edit"),

]
