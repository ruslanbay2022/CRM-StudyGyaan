from django.urls import path, include
from apps.userprofile.views import ProfileView, ProfileUpdateView

urlpatterns = [
	path('', ProfileView.as_view(), name='ProfileView'),
	path('update/', ProfileUpdateView.as_view(), name='ProfileUpdateView'),
]