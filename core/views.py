from django.shortcuts import render
from core.models import MainInfo, Service, Promotion, Contact, Effect, HowItWork


def main(request):
    infos = MainInfo.objects.all()
    services = Service.objects.filter(is_active=True, on_main=True)
    contacts = Contact.objects.all()
    effects = Effect.objects.filter(on_main=True)
    howitworks = HowItWork.objects.filter(on_main=True)
    return render(
        request,
        "core/main.html",
        {
            "info1": infos[:3],
            "info2": infos[3:6],
            "services": services,
            "contacts": contacts,
            "effects": effects,
            "howitworks": howitworks,
        },
    )


def price(request):
    services = Service.objects.all()
    promotions = Promotion.objects.all()
    promotion_types = Promotion.PROMOTION_TYPES
    return render(
        request,
        "core/prices.html",
        {
            "services": services,
            "promotions": promotions,
            "promotion_types": promotion_types,
        },
    )
