from django.contrib import admin
from .models import MainInfo, Service, Promotion, Review, Contact


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'description', 'price', 'on_main', 'is_active']
    list_editable = ['on_main', 'is_active']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'duration', 'description', 'price', 'is_active']
    list_editable = ['is_active']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'rating', 'moderated', 'on_main']


admin.site.register(Contact)
admin.site.register(MainInfo)
