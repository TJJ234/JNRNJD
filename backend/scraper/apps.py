from django.apps import AppConfig

# Leave this import so we can run the tasks file
from .tasks import CAR_DATA_URL

class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraper'
