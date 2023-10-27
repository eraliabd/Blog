from django.urls import path
from .views import post_view, detail, PostView

urlpatterns = [
    path('', post_view, name='index'),
    path('myblog/', PostView.as_view(), name='blog'),
    path('detail/<int:pk>/', detail, name='detail'),
]
