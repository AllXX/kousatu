from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',RedirectView.as_view(url='/app')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
