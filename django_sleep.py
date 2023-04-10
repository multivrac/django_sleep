"""
This module provides very simple Django middleware that sleeps on every request.

This is useful when you want to simulate slow response times (as might be
encountered, say, on a cell network).

To use, add this middleware, and add a value for SLEEP_TIME to your settings.

Tested on django 4.1.7
"""

import time
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class SleepMiddleware(MiddlewareMixin):

    def process_request(self, request):
        slowdown = getattr(settings, "SLEEP_TIME", 2)
        if slowdown > 0:
            time.sleep(slowdown)
    
