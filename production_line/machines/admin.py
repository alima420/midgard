from django.contrib import admin
from .models import Machine, LogisticsBox, Exception, ProductBox

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'program', 'counter')
    
@admin.register(LogisticsBox)
class LogisticsBoxAdmin(admin.ModelAdmin):
    list_display = ('logistics_box_id', 'details', 'flag',)

@admin.register(Exception)
class ExceptionAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'logistics_box', 'details', 'flag',)
    list_filter = ('logistics_box',)

@admin.register(ProductBox)
class ProductBoxAdmin(admin.ModelAdmin):
    list_display = ('product_serial', 'logistics_box_id', 'logistics_box_timestamp', 'number_units', 'article_number', 'product_box_id', 'device_creation_timestamp', 'device_remarks')
    list_filter = ('logistics_box_id',)
    list_per_page = 36