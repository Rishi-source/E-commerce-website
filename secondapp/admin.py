from django.contrib import admin
from secondapp.models import (Contact_Us,Category,
register_table,add_product,cart,Order,balance,wishlist,Review)
from import_export.admin import ImportExportModelAdmin
from . import models
admin.site.site_header="My Website | Second Project"

class Contact_UsAdmin(admin.ModelAdmin):
    fields = ["contact_number","name","subject","message"]

    list_display = ["id","name","contact_number","subject","message","added_on"]
    search_fields = ["name"]
    list_filter = ["added_on","name"]
    list_editable = ["name"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","cat_name","description","added_on"]

class OrderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
           ...
admin.site.register(models.Order , OrderAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(register_table)
admin.site.register(add_product)
admin.site.register(cart)
admin.site.register(balance)
admin.site.register(wishlist)
admin.site.register(Review)

