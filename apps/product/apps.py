from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'apps.product'
    
    def ready(self):
        import apps.product.translation  # noqa: F401
    verbose_name = 'Все товары и всё прочее'
