from __future__ import absolute_import, unicode_literals

# This ensures the app is always imported when
# Django starts so that shared tasks work correctly.
from .celery import app as celery_app

__all__ = ('celery_app',)