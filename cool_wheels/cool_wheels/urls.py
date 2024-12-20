from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, shop


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="homepage"),
    path("shop/", shop, name="shop"),
    path("brand/<slug:brand_slug>/", home, name="brand_filter"),
    path("shop/brand/<slug:brand_slug>/", shop, name="shop_brand_filter"),
    path("", include("users.urls")),
    path("", include("cars.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
