from django.contrib import admin
from django.urls import path, include
from shortener.views import redirect_short_link

urlpatterns = [
    path('admin/', admin.site.urls),
    path('links/', include('shortener.urls')),
    path('<str:short_code>/', redirect_short_link, name='redirect-short-link'),
]
