from django.urls import  path
from .views import (
    ApiListApiView,
    ApiDetailApiView,
    UserLoginAPIView
)

urlpatterns = [
    path('api/', ApiListApiView.as_view()),
    path('api/<int:api_id>/', ApiDetailApiView.as_view()),
    path('api/login/', UserLoginAPIView.as_view(), name='api_login'),

]
