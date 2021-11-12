from django.urls import include, path
from . import views
from . views import index,Map_View,Article_View,Contact_view

urlpatterns  = [
	path('', index.as_view(), name='index' ),
	path('mapView', Map_View.as_view(), name='mapView' ),
	path('articleView', Article_View.as_view(), name='articleView' ),
	path('contact', Contact_view.as_view(), name='contact' ),
	path('getMapView/', views.GetMapView, name='getMapView' ),
	path('getmainView', views.GetMainView, name='getmainView' ),
	]