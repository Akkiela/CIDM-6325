from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path(
        'detail/<int:id>/<slug:slug>/',
        views.image_detail,
        name='detail',
    ),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
    path('recipeList/', views.recipe_list,name='recipe_list'),
    path('bookmark/<int:recipe_id>/',views.bookmark_image,name='bookmark_image'),
    path('bookmarks/', views.user_bookmarks,name='user_bookmarks'),
]