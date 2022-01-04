from django.shortcuts import render
from core.models import MainInfo, Service, Promotion, Review, Contact, Effect, HowItWork

# Create your views here.


def main(request):
    infos = MainInfo.objects.all()
    services = Service.objects.filter(is_active=True, on_main=True)
    reviews = Review.objects.all()
    contacts = Contact.objects.all()
    effects = Effect.objects.all()
    howitworks = HowItWork.objects.all()
    return render(
        request,
        "core/main.html",
        {
            "info1": infos[:3],
            "info2": infos[3:6],
            "services": services,
            "reviews": reviews,
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


def review(request):
    reviews = Review.objects.all()
    return render(
        request,
        "core/reviews.html",
        {
            "reviews": reviews,
        },
    )


def contact(request):
    contacts = Contact.objects.all()
    return render(
        request,
        "core/contacts.html",
        {
            "contacts": contacts,
        },
    )
