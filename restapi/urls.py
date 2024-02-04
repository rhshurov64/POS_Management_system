from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register(r'viewset_api', views.StudentModelViewSet, basename='viewset_api')
router.register(r'category', views.CategoryModelViewset, basename='category')
router.register(r'product', views.ProductModelViewset, basename='product')

urlpatterns = [
    path('student_api/', views.student_api, name='student_api'),
    path('student_api/<int:id>/', views.student_api, name='student_api'),
    path('class_api/', views.class_api.as_view(), name='class_api'),
    path('class_api/<int:pk>/', views.class_api.as_view(), name='class_api'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]