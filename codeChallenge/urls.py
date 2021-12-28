from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.conf import settings

from codeApp.views import LandingPageView
from security.views import secret_key_page, pickling_page

urlpatterns = [
    # Apps
    path('admin/', admin.site.urls),
    path('', include('codeApp.urls', namespace='codeApp')),
    path('', include('jSon.urls', namespace='json')),
    path('theater/', include('theater.urls', namespace='theater')),
    # Landing Page
    path('', LandingPageView.as_view(), name='landing-view'),
    path('security/secret_key', secret_key_page),
    path('security/pickling', pickling_page),
    # Auth
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)