from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.showformdata),
    path('completed/', views.completed),

]