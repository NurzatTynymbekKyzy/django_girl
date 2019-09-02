from django.urls import path
from blog.views import get_index, post_detail,post_new, post_edit

urlpatterns = [
    path('', get_index, name='index'),
    path('<int:pk>/',post_detail,name='post_detail'),
    path('new/',post_new,name='post_new'),
    path('<int:pk>/edit/', post_edit, name='post_edit'),
]


