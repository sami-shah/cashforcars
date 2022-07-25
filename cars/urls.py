
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('cashforallcars/', views.cashforallcars, name='cashforallcars'),
    path('cashforcars/', views.cashforcars, name='cashforcars'),
    path('contact/', views.contact, name='contact'),
    path('getquote/', views.getquote, name='getquote'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
