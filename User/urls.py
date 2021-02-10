from django.urls import path, include

from User.views import UserByToken

urlpatterns = [
    path('user/by/token/', UserByToken.as_view()),
]