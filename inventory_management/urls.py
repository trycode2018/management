from rest_framework.routers import SimpleRouter
from inventory_management.views.views_category import CategoryView
from inventory_management.views.views_supplier import SupplierView
from inventory_management.views.views_product import ProductView

router = SimpleRouter()
router.register('categories',CategoryView)
router.register('products',ProductView)
router.register('suppliers',SupplierView)


