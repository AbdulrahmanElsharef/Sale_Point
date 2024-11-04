from django.contrib import admin
from invoice.models import (Profile, Party, ItemService, Sale,
                            Transaction)
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["__str__","name","phone","address","reg_no"]
    list_filter=["name","phone","address","reg_no"]
@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ["__str__","name","phone","address","balance_amount"]
    list_filter=["name","phone","address","balance_amount"]
@admin.register(ItemService)
class ItemServiceAdmin(ImportExportModelAdmin):
    list_display = ["__str__","name","des","item_type","quantity","price","discount"]
    list_filter=["name","item_type","quantity","price","discount"]
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["__str__","bill_date","total_amount","amount_paid","remaining_balance"]
    list_filter=["id","bill_date","party__name","party__phone","total_amount","amount_paid","remaining_balance"]
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["__str__","sales","item","price","quantity","amount","discount_percent"]
    list_filter= ["sales__id","sales__party__name","sales__party__phone","item","price","quantity","amount","discount_percent"]

