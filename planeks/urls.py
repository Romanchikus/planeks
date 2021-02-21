from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import handler404
from schemas import views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("accounts/", include("django.contrib.auth.urls")),
        path('signup/', views.SignupPageView.as_view(), name='signup'),
        path("", include("schemas.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

# handler404 = views.handler_404