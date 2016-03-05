from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from models import Group, Event, GroupPosting, Comment
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
def search_by_category(model_type, category):
    pass

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

def login_view(request):
    return render(request, 'envgroups/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'envgroups/index.html')

def signup_view(request):
    return render(request, 'envgroups/signup.html')

def signup_complete(request):
    username = request.POST['username']
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    if password != password_repeat:
        return render(request, 'envgroups/password_doesnt_match.html')
    else:
        user = User.objects.create_user(username=username, password=password, email=email, first_name = first_name, last_name=last_name)
        user.save()
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        return render(request, 'envgroups/user_created.html')

def about(request):
    return render(request, 'envgroups/about.html')

def groups(request, group_id=''):
#    GROUPS = Group.objects.order_by('title')
    context = {}
    GROUPS = Group.objects.order_by('title')
    cat_dic = {'':'',
               'FO':'food',
               'SO':'social',
               'EN':'energy',
               'AC':'activism',
               'EV':'environment',
               'PR':'projects',
               'AR':'arts',
               'ED':'education',
               'PO':'policy' }
    context['cat_dic'] = cat_dic
    context['detail'] = False
    if group_id == '':
        if request.method == 'POST':
            gtype = request.POST.get('group-type')
            cat = request.POST.get('group-category')
            category = cat_dic[cat]
            search_term = request.POST.get('search_term')
            if gtype != '':
                GROUPS = Group.objects.filter(gtype=gtype)
            if category != '':
                new_groups = []
                for G in GROUPS:
                    if category in G.categories():
                        new_groups.append(G)
                GROUPS = new_groups
            if search_term != '':
                new_groups = []
                for G in GROUPS:
                    if search_term.lower() in G.searchblob():
                        new_groups.append(G)
                GROUPS = new_groups
    else:
        context['detail'] = True
        GROUPS = Group.objects.filter(id=group_id)
        GROUP_POSTINGS = GroupPosting.objects.filter(groupid=int(group_id))
        context['grouppostings'] = GROUP_POSTINGS
        if request.method == 'POST': 
            if request.POST['top_level'] == "True":
                groupid = request.POST['group_id']
                username = request.POST['username']
                title = request.POST['title']
                content = request.POST['content']
                time = datetime.now()
                gp = GroupPosting(groupid=groupid, username=username, title=title, content=content, time=time)
                gp.save()
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


