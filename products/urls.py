from rest_framework.routers import SimpleRouter
from .views import ProductView

root = SimpleRouter()
root.register('products',ProductView)