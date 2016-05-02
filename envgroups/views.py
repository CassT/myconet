from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from models import Group, Event, GroupPosting, Comment, Profile,  ProjectPosting, Project
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
def cat_view(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data.get('categories')
            # do something with your results
    else:
        form = CatForm

    return render_to_response('/', {'form':form },
        context_instance=RequestContext(request))

def search_by_category(model_type, category):
    pass

def index(request):
    context = {'groupcount':str(Group.objects.count())}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'envgroups/index.html', context)
                # redirect to success page
            else:
                # redirect to failed disabled account page
                pass
        else:
            # redirect to invalid login page
            return render(request, 'envgroups/index.html', context)
    gcount = Group.objects.count()
    #context = {'group_count':gcount}
    context = {}
    context['groupcount'] = str(gcount)
    return render(request, 'envgroups/index.html', context)

def login_view(request): 
    return render(request, 'envgroups/login.html') #return redirect('/login/')

def logout_view(request):
    logout(request)
    return redirect('/') #render(request, 'envgroups/index.html')

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
#        return render(request, 'envgroups/user_created.html')
        redirect_url = '/profile/%s/' % ( username )
        return redirect(redirect_url)
def about(request):
    return render(request, 'envgroups/about.html')

def blog(request):
    return render(request, 'envgroups/blog.html')

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
               'PO':'policy',
               'HO':'housing',
               'WE':'wellness',
               'RE':'research' }
    TYPES = (
        ('SG','Academic'),
        ('FP','Business'),
        ('NP','Non Profit'),
        ('GV','Government'),
        ('UC','Unclassified'),
    )
    context['type_dic'] = TYPES
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


def create_profile(request):
    categories = ['food', 'social', 'energy', 'activism', 'environment','projects', 'arts', 'education', 'policy', 'wellness', 'housing', 'research']
    skills = ['Teaching','Green_Building', 'Construction', 'Site_Planning', 'Gardening', 'Energy_Installation', 'Aquaponics_Hydroponics', 'Composting', 'Local_Ecology_Knowledge', 'Animal_Husbandry', 'Automotive_Maintenance', 'Herbal_Medicine', 'Bodywork_Breathwork', 'Acupuncture', 'Sound_Healing', 'Music', 'Painting', 'Sculpture', 'Dance_Performance', 'Cooking', 'Children_Programs', 'Planning_Coordination', 'Disruptive_Action', 'Facilitation', 'Local_Community_Knowledge', 'Grant_Writing', 'Digital_Media', 'Web_Development', 'Journalism', 'Promoting', 'Audio_Video_Engineering', 'Legal_Regulations', 'Legal_Defense', 'Manual_Labor', 'Photography']
    resources = ['Tools_Construction', 'Tools_Farming', 'Tools_Art', 'Earthmoving_Equipment', 'Construction_Materials_Structural', 'Construction_Materials_Electrical', 'Construction_Materials_Finishing', 'Construction_Materials_Plumbing', 'Art_Supplies', 'Plant_Starts', 'Seeds', 'Compost_Manure_Mulch', 'Domestic_Animals', 'Aquaponics_Hydroponics', 'Lights', 'Pots', 'Land_Agriculture', 'Land_Housing', 'Community_Space', 'Money', 'Vehicle', 'Energy_Generation']
    context ={}# {'categories':categories,}
    context['cats'] = categories
    context['skis'] = skills
    context['ress'] = resources
    if request.user.is_authenticated:
        return render(request, 'envgroups/create_profile.html', context)
    else:
        return redirect('/')
        #return render(request, 'envgroups/index.html')
    #pass
    #username = request.POST.get('username')
   
def profile_created(request):
    user = request.user
    username = user.username
    tagline = request.POST.get('tagline')
    location = request.POST.get('location')
    interests = request.POST.getlist('interests[]')
    other_interests = request.POST.get('other_interests')
    skills = request.POST.getlist('skills[]')
    #other_skills = request.POST.get('other_skills')
    resources = request.POST.getlist('resources[]')
    #other_resources = request.POST.get('other_resources')
    wdywtd = request.POST.get('wdywtd')
    needs = request.POST.get('needs')
    offerings = request.POST.get('offerings')
    ideal_collaboration = request.POST.get('ideal_collaboration')
    profile = Profile(username=username, tagline=tagline, location=location, other_interests=other_interests, wdywtd=wdywtd, needs=needs, offerings=offerings, ideal_collaboration=ideal_collaboration)
    for cat in interests:
        setattr(profile, cat, True)
    for ski in skills:
        setattr(profile, ski, True)
    for res in resources:
        setattr(profile, res, True)
    profile.save()
    redirect_url = '/profile/%s' % (username)
    return redirect(redirect_url) 
    #return render(request, 'envgroups/your_profile.html')    

def profiles(request):
    PROFILES = Profile.objects.all()
    context = {'profiles':PROFILES}
    return render(request, 'envgroups/profiles.html', context) 

def profile(request, username=''):
    logged_in_user = request.user
    if username == logged_in_user.username:
        own_profile = True
    else:
        own_profile = False
    if Profile.objects.filter(username=username).count() == 1:
        req_profile = Profile.objects.filter(username=username)[0]
    else:
        req_profile = False
    context = {'profile':req_profile, 'own':own_profile }
    return render(request, 'envgroups/profile.html', context)

def edit_profile(request, username=''):
    logged_in_user = request.user
    if username == logged_in_user.username:
        own_profile = True
    else:
        own_profile = False
    categories = ['food', 'social', 'energy', 'activism', 'environment','projects', 'arts', 'education', 'policy', 'wellness', 'housing', 'research']
    skills = ['Teaching','Green_Building', 'Construction', 'Site_Planning', 'Gardening', 'Energy_Installation', 'Aquaponics_Hydroponics', 'Composting', 'Local_Ecology_Knowledge', 'Animal_Husbandry', 'Automotive_Maintenance', 'Herbal_Medicine', 'Bodywork_Breathwork', 'Acupuncture', 'Sound_Healing', 'Music', 'Painting', 'Sculpture', 'Dance_Performance', 'Cooking', 'Children_Programs', 'Planning_Coordination', 'Disruptive_Action', 'Facilitation', 'Local_Community_Knowledge', 'Grant_Writing', 'Digital_Media', 'Web_Development', 'Journalism', 'Promoting', 'Audio_Video_Engineering', 'Legal_Regulations', 'Legal_Defense', 'Manual_Labor', 'Photography']
    resources = ['Tools_Construction', 'Tools_Farming', 'Tools_Art', 'Earthmoving_Equipment', 'Construction_Materials_Structural', 'Construction_Materials_Electrical', 'Construction_Materials_Finishing', 'Construction_Materials_Plumbing', 'Art_Supplies', 'Plant_Starts', 'Seeds', 'Compost_Manure_Mulch', 'Domestic_Animals', 'Aquaponics_Hydroponics', 'Lights', 'Pots', 'Land_Agriculture', 'Land_Housing', 'Community_Space', 'Money', 'Vehicle', 'Energy_Generation']
    #context ={}# {'categories':categories,}
    context = {'own':own_profile }
    context['cats'] = categories
    context['skis'] = skills
    context['ress'] = resources
    if request.user.is_authenticated:
        return render(request, 'envgroups/edit_profile.html', context)
    else:
        return redirect('/')

def profile_edited(request):
    user = request.user
    username = user.username
    tagline = request.POST.get('tagline')
    location = request.POST.get('location')
    interests = request.POST.getlist('interests[]')
    other_interests = request.POST.get('other_interests')
    skills = request.POST.getlist('skills[]')
    #other_skills = request.POST.get('other_skills')
    resources = request.POST.getlist('resources[]')
    #other_resources = request.POST.get('other_resources')
    wdywtd = request.POST.get('wdywtd')
    needs = request.POST.get('needs')
    offerings = request.POST.get('offerings')
    ideal_collaboration = request.POST.get('ideal_collaboration')
    profile = Profile(username=username, tagline=tagline, location=location, other_interests=other_interests, wdywtd=wdywtd, needs=needs, offerings=offerings, ideal_collaboration=ideal_collaboration)
    for cat in interests:
        setattr(profile, cat, True)
    for ski in skills:
        setattr(profile, ski, True)
    for res in resources:
        setattr(profile, res, True)
    profile.save()
    redirect_url = '/profile/%s' % (username)
    return redirect(redirect_url)

def projects(request, project_id=''):
#    GROUPS = Group.objects.order_by('title')
    context = {}
    PROJECTS = Project.objects.order_by('title')
    cat_dic = {'':'',
               'FO':'food',
               'SO':'social',
               'EN':'energy',
               'AC':'activism',
               'EV':'environment',
               'PR':'projects',
               'AR':'arts',
               'ED':'education',
               'PO':'policy',
               'HO':'housing',
               'WE':'wellness',
               'RE':'research' }
    TYPES = (
        ('SG','Academic'),
        ('FP','Business'),
        ('NP','Non Profit'),
        ('GV','Government'),
        ('UC','Unclassified'),
    )

    ski_dic = {'':'',
               'GB': 'Green_Building',
               'CT': 'Construction',
               'SP': 'Site_Planning',
               'GA': 'Gardening',
               'EI': 'Energy_Installation',
               'AQ': 'Aquaponics_Hydroponics',
               'CM': 'Composting',
               'LE': 'Local_Ecology_Knowledge',
               'AH': 'Animal_Husbandry',
               'AM': 'Automotive_Maintenance',
               'HM': 'Herbal_Medicine',
               'BW': 'Bodywork_Breathwork',
               'AP': 'Acupuncture',
               'SH': 'Sound_Healing',
               'MU': 'Music',
               'PA': 'Painting',
               'SC': 'Sculpture',
               'DP': 'Dance_Performance',
               'CK': 'Cooking',
               'CP': 'Children_Programs',
               'PC': 'Planning_Coordination',
               'DA': 'Disruptive_Action ',
               'FA': 'Facilitation',
               'LC': 'Local_Community_Knowledge',
               'GW': 'Grant_Writing',
               'TE': 'Teaching',
               'DM': 'Digital_Media',
               'WD': 'Web_Development',
               'JO': 'Journalism',
               'PM': 'Promoting',
               'AV': 'Audio_Video_Engineering',
               'LR': 'Legal_Regulations',
               'LD': 'Legal_Defense',
               'ML': 'Manual_Labor',
               'PH': 'Photography' }

    res_dic = {'':'',
               'TC': 'Tools_Construction',
               'TF': 'Tools_Farming',
               'TA': 'Tools_Art',
               'EE': 'Earthmoving_Equipment',
               'MS': 'Construction_Materials_Structural',
               'ME': 'Construction_Materials_Electrical',
               'MF': 'Construction_Materials_Finishing',
               'MP': 'Construction_Materials_Plumbing',
               'AS': 'Art_Supplies',
               'PS': 'Plant_Starts',
               'SE': 'Seeds',
               'MM': 'Compost_Manure_Mulch',
               'DO': 'Domestic_Animals',
               'AY': 'Aquaponics_Hydroponics',
               'LI': 'Lights',
               'PT': 'Pots',
               'LA': 'Land_Agriculture',
               'LH': 'Land_Housing',
               'CS': 'Community_Space',
               'MO': 'Money',
               'VE': 'Vehicle',
               'EG': 'Energy_Generation' }

    context['type_dic'] = TYPES
    context['cat_dic'] = cat_dic
    context['detail'] = False
    context['ski_dic'] = ski_dic
    context['res_dic'] = res_dic
    if project_id == '':
        if request.method == 'POST':
            ptype = request.POST.get('project-type')
            cat = request.POST.get('project-category')
            category = cat_dic[cat]
            search_term = request.POST.get('search_term')
            if ptype != '':
                PROJECTS = Project.objects.filter(ptype=ptype)
            if category != '':
                new_projects = []
                for P in PROJECTS:
                    if category in P.categories():
                        new_projects.append(P)
                PROJECTS = new_projects
            if search_term != '':
                new_projects = []
                for P in PROJECTS:
                    if search_term.lower() in P.searchblob():
                        new_projects.append(P)
                PROJECTS = new_projects
    else:
        context['detail'] = True
        PROJECTS = Project.objects.filter(id=project_id)
        PROJECT_POSTINGS = ProjectPosting.objects.filter(projectid=int(project_id))
        context['projectpostings'] = PROJECT_POSTINGS
        if request.method == 'POST':
            if request.POST['top_level'] == "True":
                projectid = request.POST['project_id']
                username = request.POST['username']
                title = request.POST['title']
                content = request.POST['content']
                time = datetime.now()
                pp = ProjectPosting(projectid=projectid, username=username, title=title, content=content, time=time)
                pp.save()
    context['projects'] = PROJECTS
    return render(request, 'envgroups/projects.html', context)

def projects2(request):
    return render(request, 'envgroups/projects2.html')
