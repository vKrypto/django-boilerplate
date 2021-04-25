"""
all config, default switch goes here.
warning: do not edit default switches here, you can  create a local version of that varaibale for your app.
"""
INSTALLED_APPS += [
    'apps.{{ app_name }}'
]

WEIGHTED_INSTALLED_APPS = [
    # (weight, app_name),
]
