from django.contrib import admin
from .models import MainInfo, Service, Promotion, Contact, Effect, HowItWork


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "duration", "description", "price", "on_main", "is_active"]
    list_editable = ["on_main", "is_active"]


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "duration", "description", "price", "is_active"]
    list_editable = ["is_active"]


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    list_display = ["name", "on_main"]
    list_editable = ["on_main"]


@admin.register(HowItWork)
class HowItWorkAdmin(admin.ModelAdmin):
    list_display = ["name", "on_main"]
    list_editable = ["on_main"]


admin.site.register(Contact)
admin.site.register(MainInfo)
