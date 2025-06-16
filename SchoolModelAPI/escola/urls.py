from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escola.views import ClientViewSet, ListaViewSet, TodoItemViewSet, TodoViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'listasssssssss', ListaViewSet)
router.register(r'todoitemsss', TodoItemViewSet)
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]