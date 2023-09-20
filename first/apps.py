from django.apps import AppConfig


class FirstConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first'
    
    def ready(self):
        import first.signals  #imported apps signals
