from django.contrib import admin
from .models import ProductModel, OfferModel, BookMarkModel

# Register your models here.
class HikakuAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductModel, HikakuAdmin)
admin.site.register(OfferModel, HikakuAdmin)
admin.site.register(BookMarkModel, HikakuAdmin)