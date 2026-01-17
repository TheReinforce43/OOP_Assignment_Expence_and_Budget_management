from django.urls import path ,include 

from rest_framework.routers import DefaultRouter

from Category.View.category_view import CategoryModelViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'categories', CategoryModelViewSet, basename='category')




# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]