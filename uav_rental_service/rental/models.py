from django.db import models

from django.db import models
from django.contrib.auth.models import User
from uav.models import UAV

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.uav} rented by {self.user} from {self.start_datetime} to {self.end_datetime}"
