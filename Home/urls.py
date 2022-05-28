from django.urls import path

from .views import index, dashboard, auth, create, settings


urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
    path('auth', auth),
    path('add', create),
    path('settings', settings)
]