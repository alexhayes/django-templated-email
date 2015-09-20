import os
import django
from distutils.version import LooseVersion

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = []

INSTALLED_APPS = (
    'templated_email',
)

TEMPLATED_EMAIL_TEMPLATE_DIR = ''

if LooseVersion(django.get_version()) >= LooseVersion("1.8"):
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(os.path.dirname(__file__), 'templated_email', ''),
            ]
        },
    ]
else:
    TEMPLATE_DIRS = [
        os.path.join(os.path.dirname(__file__), 'templated_email', ''),
    ]



SECRET_KEY = "notimportant"
