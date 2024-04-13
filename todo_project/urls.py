from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated
from todo.views import TodoItemViewSet

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'todo', TodoItemViewSet, basename='todo')

# Wire up our API using automatic URL routing
# Additionally, include login URLs for the browsable API
urlpatterns = [
    path('api/', include(router.urls)),
]

# Set the default permission class for the API
# This will ensure that all API endpoints require authentication
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
