from .views import SupplierView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('suppliers',SupplierView)


