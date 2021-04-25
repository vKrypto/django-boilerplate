"""
override any swicth or config here, or declare a final variable here..
"""
from django.core.exceptions import ImproperlyConfigured


def sort_by_weight(weighted_list):
    """ takes a weighted list and return list in order """
    sorted_list = []
    try:
        for entry in sorted(weighted_list):
            if len(entry)==2:
                _, app_name = entry
                if isinstance(app_name,(str)):
                    sorted_list.append(app_name)
    except ValueError as e:
        raise ImproperlyConfigured("please define weighted_vaLues as =>> (3, 'value...') ")
    return sorted_list[::-1]




# now redefine installed apps.
INSTALLED_APPS = CORE_INSTALLED_APPS + sort_by_weight(WEIGHTED_INSTALLED_APPS) + INSTALLED_APPS

# now redefine installed apps.
MIDDLEWARE = CORE_MIDDLEWARE + sort_by_weight(WEIGHTED_MIDDLEWARE) + MIDDLEWARE
