from django.apps import AppConfig




class WeatherappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weatherapp'


def ready(self):
    from .templates import register_templates
    register_templatesweather(weather.html)