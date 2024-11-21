from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # Post views
    path('', views.post_list, name='post_list'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path(
        'tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail,
        name='post_detail',
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:recipe>/',
        views.recipe_detail,
        name='recipe_detail',
    ),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:recipe_id>/share/', views.recipe_share, name='recipe_share'),
    path(
        '<int:post_id>/comment/', views.post_comment, name='post_comment'
    ),
    path(
        '<int:recipe_id>/comment/', views.recipe_comment, name='recipe_comment'
    ),
    path(
        '<int:post_id>/rating/', views.post_rating, name='post_rating'
    ),
    path(
        '<int:recipe_id>/rating/', views.recipe_rating, name='recipe_rating'
    ),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
