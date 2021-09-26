from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_post, name='home'),
    path('<int:id>', views.details, name='post_details'),
]
