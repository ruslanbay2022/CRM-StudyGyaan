from django.urls import path, include
from apps.children.views import ChildrenView, ChildDetailsView, ChildUpdateView, ChildCreateView, ChildrenArchivedView, \
	GirlsView, BoysView, ChildDeleteView

urlpatterns = [
	path('', ChildrenView.as_view(), name='ChildrenView'),
	path('archive/', ChildrenArchivedView.as_view(), name='ChildrenArchivedView'),
	path('girls/', GirlsView.as_view(), name='GirlsView'),
	path('boys/', BoysView.as_view(), name='BoysView'),
	path('add/', ChildCreateView.as_view(), name="ChildCreateView"),
	path('<int:pk>/', ChildDetailsView.as_view(), name="ChildDetailsView"),
	path('<int:pk>/update/', ChildUpdateView.as_view(), name="ChildUpdateView"),
	path('<int:pk>/delete/', ChildDeleteView.as_view(), name='ChildDeleteView'),
]