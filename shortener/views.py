from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Link.objects.filter(created_by=user)
        return Link.objects.none()
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(created_by=self.request.user)
        else:
            serializer.save()


def redirect_short_link(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    link.click_count += 1
    link.save()
    return redirect(link.original_url)


