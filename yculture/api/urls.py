from django.urls import include, path
from .views import (
    ApiListApiView,
    ApiDetailApiView
)

urlpatterns = [
    path('api/', ApiListApiView.as_view()),
    path('api/<int:api_id>/', ApiDetailApiView.as_view()),

]
