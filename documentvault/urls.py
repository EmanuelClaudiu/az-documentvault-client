from django.contrib import admin
from django.urls import path
from documentvault import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_file, name='upload_file'),
]
