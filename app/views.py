from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topics.html',d)
def display_webpages(request):
    WLTO=Webpage.objects.all()
    d={'webpage':WLTO}
    return render(request,'display_webpages.html',d)
def display_accessread(request):
    ALTO=AccessRead.objects.all()
    d={'accessread':ALTO}
    return render(request,'display_access.html',d)