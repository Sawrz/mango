from django.contrib.auth.models import User
from django.conf import settings


def project_context(request):

    context = {
        'me': User.objects.first(),
    }

    return context

def root_url(request):
    """
    Pass your root_url from the settings.py
    """

    return {'ROOT_URL': settings.ROOT_URL}
