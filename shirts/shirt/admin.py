from django.contrib import admin

# Register your models here.
from shirt.models import Product, Product_Varients, Sno


class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["product_name", "product_id", "product_price"]
	list_display_links = ["product_name"]
	list_filter = ["product_name", "product_price"]
	search_fields = ["product_name", "product_id"]
	class Meta:
		model = Product

class Product_VarientsModelAdmin(admin.ModelAdmin):
	list_display = ["SKU_Code", "product_id", "size"]
	list_display_links = ["product_id"]
	list_filter = ["product_id", "size"]
	search_fields = ["SKU_Code", "product_id", "size"]
	class Meta:
		model = Product

class SnoModelAdmin(admin.ModelAdmin):
	list_display = ["product_id"]
	list_display_links = ["product_id"]
	list_filter = ["product_id"]


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Product_Varients, Product_VarientsModelAdmin)
admin.site.register(Sno, SnoModelAdmin)
