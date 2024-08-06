from django.urls import path,include
from . import views
urlpatterns = [
    
    path('login/',views.login_view,name='display'),
    path('auth/',views.auth_view,name='auth'),
    path('create/',views.createUser , name='create'),
    path('update/',views.update,name='update'),
    path('register/', views.register, name='register'),
]
