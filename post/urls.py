from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, MyLoginView

app_name = 'post'

urlpatterns = [
    path('list/', PostList.as_view(), name='post_list'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path('login/', MyLoginView.as_view(), name='login'),
]
