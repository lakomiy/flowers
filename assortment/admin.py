from django.contrib import admin

# Register your models here.
from .models import Assortment, Category

class AssortmentAdmin(admin.ModelAdmin):
    list_display = ("name_product","price_product","create_at","category")
    list_display_links = ("name_product",)
    search_fields = ("name_product", "description_product", "create_at", "price_product")

admin.site.register(Assortment,AssortmentAdmin)
admin.site.register(Category)

