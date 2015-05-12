import urllib

from django.conf import settings

def global_vars(request):
    return {
        'BASE_URL': getattr(settings, 'BASE_URL', ""),
        'DEBUG': getattr(settings, 'DEBUG', ""),
    }