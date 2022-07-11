from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shows/', views.shows_index, name='index'),
    path('shows/<int:show_id>/', views.shows_detail, name='detail'),
    path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
    path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
    path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
    path('categories/<int:show_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
    path('categories/<int:show_id>/assoc_category/<int:category_id>/delete/', views.assoc_category_delete,
    name='assoc_category_delete'),
    path('categories/', views.CategoryList.as_view(), name='categories_index'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='categories_detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='categories_delete'),
    path('shows/<int:show_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
    path('accounts/signup/', views.signup, name='signup'),
    path('shows/<int:show_id>/add_photo/', views.add_photo, name='add_photo'),
]