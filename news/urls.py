from django.urls import path
from .views import PostsList, PostsDetail, PostsSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostsDetail.as_view(), name='post_detail'),
    path('search/', PostsSearch.as_view(), name='search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
]
