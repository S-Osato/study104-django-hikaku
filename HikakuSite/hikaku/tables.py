import django_tables2 as tables
from .models import ProductModel
from django_tables2.utils import A
from django.utils.html import format_html

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<a href="{}">画像リンク</a>', value)
    
class ProductTable(tables.Table):
    image_link = ImageColumn()
    
    class Meta:
        model = ProductModel
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "price", "image_link")