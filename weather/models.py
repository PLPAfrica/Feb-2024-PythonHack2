from django.db import models
import logging

logger = logging.getLogger(__name__)


class WeatherData(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.FloatField()
    conditions = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    condition_icon = models.CharField(max_length=100, default=0)
=======
>>>>>>> 16c2ba80e260c150282793b09eb0f68829f43666

    def __str__(self):
        try:
            return f"Weather in {self.location} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {self.temperature} °C, {self.conditions}"
        except Exception as e:
            logger.error("Error formatting WeatherData string representation: %s\n%s", e, e.__traceback__)
            return super().__str__()
