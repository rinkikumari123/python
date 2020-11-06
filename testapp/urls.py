from django.urls import path
from .views import LoginAPI ,RegisterAPI
from knox import views as knox_views
from .import views

urlpatterns=[path("data/",views.student_detail),
path("detail/<int:pk>/",views.student_all_detail),
#path("register/",views.admin_registration),
path("regdetail/<int:pk>/",views.admin_all_detail),
path('register/', RegisterAPI.as_view(), name='register'),
path('login/', LoginAPI.as_view(), name='login'),
path('logout/', knox_views.LogoutView.as_view(), name='logout'),]
