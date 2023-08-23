
from django.contrib import admin
from django.urls import path,include
#from categories.urls import router
#from suppliers.urls import router as supplier
#from products.urls import root 
from inventory_management.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('rest_framework.urls')),
    path('api/v1/',include(router.urls))
]
