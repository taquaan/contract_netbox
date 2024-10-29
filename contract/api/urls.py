from netbox.api.routers import NetBoxRouter
from . import views

app_name = "contract"

router = NetBoxRouter()
router.register('contracts', views.ContractViewSet)
router.register('suppliers', views.SupplierViewSet)

urlpatterns = router.urls