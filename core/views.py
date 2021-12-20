from django.shortcuts import render

from core.models import MainInfo, Service

# Create your views here.


def info_view(request):
    infos = MainInfo.objects.all()
    services = Service.objects.all()
    return render(request, 'core/base.html', {'infos': infos,
                                              'services': services})
