from django.contrib import admin
from django.urls import path
from accounts.views import signup

from yculture import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
]
