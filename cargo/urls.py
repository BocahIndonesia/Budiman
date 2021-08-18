from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('login/<str:username>/<str:password>', views.validasi, name='validasi'),
	path('home/<int:id_akun>/', views.home, name='home'),
]