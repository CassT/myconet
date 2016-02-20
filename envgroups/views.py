from django.shortcuts import render
from django.contrib.auth import authenticate, login
from models import Group, Event
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'envgroups/index.html')
                # redirect to success page
            else:
                # redirect to failed disabled account page
                pass
        else:
            # redirect to invalid login page
            return render(request, 'envgroups/index.html')
    return render(request, 'envgroups/index.html')

def about(request):
    return render(request, 'envgroups/about.html')

def groups(request):
    GROUPS = Group.objects.order_by('title')
    context = {}
    if request.method == 'POST':
        gtype = request.POST.get('group-type')
        category = request.POST.get('group-category')
        search_term = request.POST.get('search_term')
        if gtype != "":
            GROUPS = Group.objects.filter(gtype = gtype)
        cat_dic = {'FO':'food',
                   'SO':'social',
                   'EN':'energy',
                   'AC':'activism',
                   'EV':'environment',
                   'PR':'projects',
                   'AR':'arts',
                   'ED':'education',
                   'PO':'policy' }
        if category != "":
            new_groups = []
            for G in GROUPS:
                if getattr(G, cat_dic[category]):
                    new_groups.append(G)
            GROUPS = new_groups
        if search_term != "":
            new_groups = []
            for G in GROUPS:
                st = search_term.lower()
                t = G.title.lower()
                m = G.mission.lower()
                if st in t or st in m:
                    new_groups.append(G)
            GROUPS = new_groups
    if request.method == 'GET' and 'group_id' in request.GET:
        present = datetime.now()
        context['getTrue'] = True
        gid = request.GET.get('group_id')
        GROUPS = Group.objects.filter(id=gid)
        EVENTS = Event.objects.filter(group=GROUPS[0].title).filter(time__gte=present).order_by('time')
        context['group_id'] = gid
        context['events'] = EVENTS
    else:
        context['getTrue'] = False 
    context['groups'] = GROUPS 
    return render(request, 'envgroups/groups.html', context)

def events(request, event_id=''):
    present = datetime.now()
    GROUPS = Group.objects.all()
    EVENTS = Event.objects.filter(time__gte=present).order_by('time')
    if request.method == 'POST':
        st = request.POST.get('search_term').lower()
        new_events = []
        for E in EVENTS:
            g = E.group.lower()
            n = E.name.lower()
            l = E.location.lower()
            d = E.description.lower()
            if st in g or st in n or st in l or st in d:
                new_events.append(E)
        EVENTS = new_events
    if request.method == 'GET' and 'event_id' in request.GET:
        eid = request.GET.get('event_id')
        if eid not in ['',None]:
            EVENTS = Event.objects.filter(id=eid)
    context = {'groups':GROUPS,
               'events':EVENTS,
               'event_id':event_id}    
    return render(request, 'envgroups/events.html', context)


