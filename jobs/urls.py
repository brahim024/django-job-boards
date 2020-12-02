from django.urls import path,include
from .import views
app_name='jobs'
urlpatterns = [
    path('', views.all_post,name='all_post'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.post, name='job_details'),
    ]