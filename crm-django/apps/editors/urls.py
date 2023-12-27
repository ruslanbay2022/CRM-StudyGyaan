from django.urls import path
from apps.editors.views import UsersListView, UsersDetailsView, UserUpdateView, UserCreateView, UserDeleteView

urlpatterns = [
	path('', UsersListView.as_view(), name='UsersListView'),
	path('<int:pk>/', UsersDetailsView.as_view(), name="UsersDetailsView"),
	path('<int:pk>/update/', UserUpdateView.as_view(), name="UserUpdateView"),
	path('add/', UserCreateView.as_view(), name="UserCreateView"),
	path('<int:pk>/delete/', UserDeleteView.as_view(), name='UserDeleteView'),
]