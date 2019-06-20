from django.urls import path, re_path

urlpatterns = [
    #Главная страница
    path('', views.index, name = "index"),

]
