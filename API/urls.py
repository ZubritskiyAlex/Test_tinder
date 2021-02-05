from django.conf.urls import url

from tinder.views import UserRetrieveUpdateAPIView
from .views import CreateUserAPIView

urlpatterns = [
    url('create/', CreateUserAPIView.as_view()),
    url('update/', UserRetrieveUpdateAPIView.as_view())
]
