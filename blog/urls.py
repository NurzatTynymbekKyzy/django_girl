from django.urls import path
from blog.views import get_index

urlpatterns = [
    path('', get_index, name='index'),
]

