from django.urls import path
from . import views

urlpatterns = [
    path('', views.collage_list, name='collage_list'),
    path('upload/', views.collage_upload, name='collage_upload'),
    path('display/<int:collage_id>/', views.collage_display, name='collage_display'),
]
