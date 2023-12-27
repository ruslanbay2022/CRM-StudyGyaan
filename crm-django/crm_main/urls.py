"""
URL configuration for crm_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from apps.common.views import (
    RegisterView,
    HomeView,
    MyLogoutView,
    DashboardView,
    MyPasswordChangeView,)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(),
         name='HomeView'),
    path('register/', RegisterView.as_view(),
         name='RegisterView'),
    path('login/', LoginView.as_view(template_name='common/login.html', redirect_authenticated_user=True),
         name="LoginView"),
    path('logout/', MyLogoutView.as_view(),
         name='MyLogoutView'),
    path('dashboard/', DashboardView.as_view(),
         name='DashboardView'),
    path('change-password/', MyPasswordChangeView.as_view(),
         name="MyPasswordChangeView"),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('profile/', include('apps.userprofile.urls')),
    path('children/', include('apps.children.urls')),
    path('editors/', include('apps.editors.urls')),
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
    urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
