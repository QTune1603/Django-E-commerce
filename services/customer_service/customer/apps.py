from django.apps import AppConfig

class CustomerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services.customer_service.customer'

    def ready(self):
        from services.customer_service.customer import signals
