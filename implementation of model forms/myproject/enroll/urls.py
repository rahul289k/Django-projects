from django.urls import path
from enroll import views


urlpatterns = [
    path('form',views.showdata),
    
]