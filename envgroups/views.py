from django.shortcuts import render
from models import Group, Event

# Create your views here.
def index(request):
    return render(request, 'envgroups/index.html')

def groups(request):
    GROUPS = Group.objects.all()
    context = {'groups':GROUPS}
    return render(request, 'envgroups/groups.html', context)

def events(request):
    GROUPS = Group.objects.all()
    EVENTS = Event.objects.all()
    context = {'groups':GROUPS,
               'events':EVENTS}
    return render(request, 'envgroups/events.html', context)
