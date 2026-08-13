from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from shortener.views import redirect_short_link


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'links': reverse('link-list', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'logout': reverse('logout', request=request, format=format),
        'note': 'To view/edit a specific link, go to /links/<id>/. To use a short link, visit /<short_code>/ directly.',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api-auth/', include('rest_framework.urls')),
    path('links/', include('shortener.urls')),
    path('account/', include('accounts.urls')),
    path('<str:short_code>/', redirect_short_link, name='redirect-short-link'),     # this must be at last
]
