from django.urls import path
from . import views

urlpatterns = [
    path('', views.collage_list, name='collage_list'),
    path('upload/', views.upload_collage, name='upload_collage'),
    path('collage/<int:collage_id>/', views.collage_display, name='collage_display'),
    path('collage/<int:collage_id>/delete/', views.delete_collage, name='delete_collage'),
]
