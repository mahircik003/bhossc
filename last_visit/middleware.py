from django.utils.timezone import now
from base.models import User
from django.utils.timezone import now
import datetime
from django.utils.timezone import utc

class LastVisit:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # User.objects.filter(id=request.user.id).update(last_time_visited = now())
            pass
        response = self.get_response(request)
        return response