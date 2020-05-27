from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user_activity import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('activities/', views.ActivityList.as_view()),
    path('activities/<int:pk>/', views.ActivityDetail.as_view()),
    path('act-user/', views.ActivityWithUserInfoList.as_view()),
    path('act-user/<int:pk>/', views.ActivityWithUserInfoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
