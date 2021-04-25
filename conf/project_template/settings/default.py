"""
all type of swicthes must here, 
assume this as default settings..
"""
import os
from django.contrib import messages



ENABLE_SILK = os.environ.get('ENABLE_SILK', False)
DJDT = os.environ.get('ENABLE_SILK', DEBUG)
GRAPHENE = os.environ.get('ENABLE_SILK', False)
REDIS = os.environ.get('ENABLE_SILK', False )

# django-sessions configs
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# django message classs
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
    messages.SUCCESS: 'success'
}

# for django:3.2 default primary key field.
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'