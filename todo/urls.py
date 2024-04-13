from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'todo', TodoItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Todo API')),
    path('schema/', get_schema_view(
        title="Todo API",
        description="API for managing todo items",
        version="1.0.0"
    ), name='openapi-schema'),
]
