
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from demo1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('user_create/', views.user_create, name='user_create'),
    path('login_tb/', views.login_tb, name='login_tb'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
