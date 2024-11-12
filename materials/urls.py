from django.urls import path, include
from rest_framework.routers import DefaultRouter
from materials.views import MaterialViewSet, CategoryViewSet, upload_materials, CategoryTreeAPIView

router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload_materials/', upload_materials, name='upload_materials'),
    path('category_tree/', CategoryTreeAPIView.as_view(), name='category_tree'),
]