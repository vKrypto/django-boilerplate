import os
# file-config
# EMAIL_URL = os.environ.get('EMAIL_URL')
# SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME')
# SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
# if not EMAIL_URL and SENDGRID_USERNAME and SENDGRID_PASSWORD:
#     EMAIL_URL = 'smtp://%s:%s@smtp.sendgrid.net:587/?tls=True' % (
#         SENDGRID_USERNAME, SENDGRID_PASSWORD)
# email_config = dj_email_url.parse(EMAIL_URL or 'console://')

# EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
# EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
# EMAIL_HOST = email_config['EMAIL_HOST']
# EMAIL_PORT = email_config['EMAIL_PORT']
# EMAIL_BACKEND = email_config['EMAIL_BACKEND']
# EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
# EMAIL_USE_SSL = email_config['EMAIL_USE_SSL']

# key-config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
ENABLE_SSL = os.environ.get('ENABLE_SSL', False)

if ENABLE_SSL:
    SECURE_SSL_REDIRECT = True
    

ROOT_EMAIL = 'developer.boilerplate@gmail.com'
ROOT_EMAIL_PASSWORD = "boilerplate@1234"


EMAIL_HOST_USER = ROOT_EMAIL
EMAIL_HOST_PASSWORD = ROOT_EMAIL_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# for creating superuser:
DJANGO_SUPERUSER_PASSWORD = ROOT_EMAIL
DJANGO_SUPERUSER_PASSWORD = ROOT_EMAIL_PASSWORD

# ADMINS = (
#     ('admin', ROOT_EMAIL),
# )
# error report emails
# MANAGERS = ADMINS

