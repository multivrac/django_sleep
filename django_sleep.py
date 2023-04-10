"""
This module provides very simple Django middleware that sleeps on every request.

This is useful when you want to simulate slow response times (as might be
encountered, say, on a cell network).

To use, add this middleware, and add a value for SLEEP_TIME to your settings.

Possible future feature: Look for an X-Django-Sleep header on each request,
to let the client specify per-request sleep time.
"""

import time

import django.conf
import django.core.exceptions
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class SleepMiddleware(MiddlewareMixin):

    def process_request(self, request):
        slowdown = getattr(settings, "SLEEP_TIME", 2)
        if slowdown > 0:
            time.sleep(slowdown)
    
