from django.apps import AppConfig


class InstaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instaapp'

    def ready(self):
        import instaapp.signals
