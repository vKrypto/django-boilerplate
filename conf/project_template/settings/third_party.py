# checkout the configurat ion and settings: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

if DJDT:
    INSTALLED_APPS += ['debug_toolbar']
    INTERNAL_IPS = ['127.0.0.1']
    # add djdt middleware at top.
    WEIGHTED_MIDDLEWARE += [
        ('0', 'debug_toolbar.middleware.DebugToolbarMiddleware'),
    ]

# Graphene-Django provides some additional abstractions that make it easy to add GraphQL functionality to your Django project.
# checkout: https://docs.graphene-python.org/projects/django/en/latest/
if GRAPHENE:
    INSTALLED_APPS += ['debug_toolbar', 'graphene_django']
    # add Graphene middleware at top.
    WEIGHTED_MIDDLEWARE += [
        ('0', 'graphene_django.debug.DjangoDebugMiddleware')
    ]

# Some cloud providers like Heroku export REDIS_URL variable instead of CACHE_URL
if REDIS:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            }
        }
    }
    CACHE_TTL = 60 * 15


if ENABLE_SILK:
    MIDDLEWARE.insert(0, 'silk.middleware.SilkyMiddleware')
    INSTALLED_APPS.append('silk')