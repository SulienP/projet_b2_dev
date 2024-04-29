from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from home.views import index
from accounts.views import signup, logout_user, login_user, settings_user
from play.views import play, contribution
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView
from django.urls import path, include

from yculture import settings
from accounts import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('getData/', views.getData, name="getData"),
    # path('post/',views.postData,name="post"),
    path('', index, name="index"),
    path('settings/', settings_user, name="settings"),
    path('play/', play, name="play"),
    path('contribution/', contribution, name="contribution"),
    path('signup/', signup, name="signup"),
    path('login/', views.login_user, name="login"),
    path('logout/' , logout_user, name="logout"),
    path('change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
