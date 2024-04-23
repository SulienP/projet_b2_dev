from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from home.views import index
from accounts.views import signup, logout_user, login_user
from play.views import play

from yculture import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('play/', play, name="play"),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/' , logout_user, name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
