from django.urls import path
from .import views
from .views import login_site


urlpatterns = [
    path('', views.home, name='home'),
    path('progress_crm/', views.index, name='index'),

    path('logout/', views.logout_site, name='logout'),
    path('login/', views.login_site, name='login'),
    path('create/', views.employee_create, name='register'),
    
    path('atendence/<str:code>/', views.attendance, name='atendence'),
]


