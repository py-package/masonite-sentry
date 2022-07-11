"""Masonite Sentry Settings"""
from masonite.environment import env

"""
|--------------------------------------------------------------------------
| Masonite Sentry
|--------------------------------------------------------------------------
|
| Sentry SDK implementation for Masonite.
|
"""

SENTRY_DSN = env("SENTRY_DSN")
SENTRY_SAMPLE_RATE = env("SENTRY_SAMPLE_RATE", "1.0")
