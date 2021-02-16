from django.urls import path
from rest_framework.routers import DefaultRouter

from dashboard import views


router = DefaultRouter()

router.register(r'bank', views.BankViewSet)
router.register(r'account', views.AccountViewSet)
router.register(r'transaction', views.TransactionViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'top_categories', views.TopCategoriesViewSet)

urlpatterns = router.urls
