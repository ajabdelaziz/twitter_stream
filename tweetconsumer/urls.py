from django.urls import re_path
from tweetconsumer import views

urlpatterns = [
    re_path(r'^signin/', views.JWTLoginView.as_view(), name='login'),
    re_path(r'^signup/', views.SignUp.as_view(), name='signup'),
    re_path(r"^tweets/", views.tweets, name="tweets"),
    re_path(r"^tweets_filtered", views.tweets_filtered, name="tweets_filtered"),
]
