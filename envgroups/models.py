from django.db import models
from django.contrib.auth.models import User

# Environmental Groups and Events
class Group(models.Model):
    BINARY_CHOICE = (
        ('Y','Yes'),
        ('N','No'),
    )
    TYPES = (
        ('SG','Academic'),
        ('FP','Business'),
        ('NP','Non Profit'),
        ('GV','Government'),
        ('UC','Unclassified'),
    )
    CATEGORIES = ['food', 'social', 'energy', 'activism', 'environment',
                  'projects', 'arts', 'education', 'policy', 'wellness', 'housing', 'research']
    food        = models.BooleanField(default=False)
    social      = models.BooleanField(default=False)
    energy      = models.BooleanField(default=False)
    activism    = models.BooleanField(default=False)
    environment = models.BooleanField(default=False)
    projects    = models.BooleanField(default=False)
    arts        = models.BooleanField(default=False)
    education   = models.BooleanField(default=False)
    policy      = models.BooleanField(default=False)
    wellness    = models.BooleanField(default=False)
    housing     = models.BooleanField(default=False)
    research    = models.BooleanField(default=False)
    title       = models.CharField(max_length=200)
    mission     = models.TextField()
    employees   = models.TextField()
    location    = models.CharField(max_length=200)
    products    = models.TextField()
    hiring      = models.CharField(max_length=1, choices=BINARY_CHOICE)
    hiring_text = models.TextField()
    gtype       = models.CharField(max_length=2, choices=TYPES)
    link        = models.CharField(max_length=300)
    connections = models.TextField()
#change types_dic for new options -t
    def group_type_label(self):
        gt = self.gtype
        types_dic = {'SG':'Academic',
                     'FP':'For Profit',
                     'NP':'Non Profit', 
                     'GV':'Government',
       		     'UC':'Unclassified',}
        gtype_label = types_dic[gt]        
        return gtype_label
    def categories(self):
        cat_list = self.CATEGORIES
        g_cat_list = []
        for cat in cat_list:
            if getattr(self, cat):
                g_cat_list.append(cat)
        return g_cat_list
    def searchblob(self):
        blob = "%s%s" % (self.title, self.mission)
        lowercaseblob = blob.lower()
        return lowercaseblob
    def __unicode__(self):
        return self.title

class Event(models.Model):
    CATEGORIES = ['food', 'social', 'energy', 'activism', 'environment',
                  'projects', 'arts', 'education', 'policy', 'wellness', 'housing', 'research']
    group       = models.CharField(max_length=200)
    name        = models.CharField(max_length=200)
    time        = models.DateTimeField()
    location    = models.TextField()
    description = models.TextField()
    link        = models.CharField(max_length=300)
    food        = models.BooleanField(default=False)
    social      = models.BooleanField(default=False)
    energy      = models.BooleanField(default=False)
    activism    = models.BooleanField(default=False)
    environment = models.BooleanField(default=False)
    projects    = models.BooleanField(default=False)
    arts        = models.BooleanField(default=False)
    education   = models.BooleanField(default=False)
    policy      = models.BooleanField(default=False)
    wellness    = models.BooleanField(default=False)
    housing     = models.BooleanField(default=False)
    research    = models.BooleanField(default=False)
    def categories(self):
        cat_list = self.CATEGORIES
        g_cat_list = []
        for cat in cat_list:
            if getattr(self, cat):
                g_cat_list.append(cat)
        return g_cat_list
    def __unicode__(self):
        s = self.time.strftime('%Y-%m-%d %H:%M ') + self.name
        return s

class Project(models.Model):
    BINARY_CHOICE = (
        ('Y','Yes'),
        ('N','No'),
    )
    TYPES = (
        ('SG','Academic'),
        ('FP','Business'),
        ('NP','Non Profit'),
        ('GV','Government'),
        ('UC','Unclassified'),
    )
    CATEGORIES = ['food', 'social', 'energy', 'activism', 'environment',
                  'projects', 'arts', 'education', 'policy', 'wellness', 'housing', 'research']
    food        = models.BooleanField(default=False)
    social      = models.BooleanField(default=False)
    energy      = models.BooleanField(default=False)
    activism    = models.BooleanField(default=False)
    environment = models.BooleanField(default=False)
    projects    = models.BooleanField(default=False)
    arts        = models.BooleanField(default=False)
    education   = models.BooleanField(default=False)
    policy      = models.BooleanField(default=False)
    wellness    = models.BooleanField(default=False)
    housing     = models.BooleanField(default=False)
    research    = models.BooleanField(default=False)

    RESOURCES = ['Tools_Construction', 'Tools_Farming', 'Tools_Art', 'Earthmoving_Equipment', 'Construction_Materials_Structural', 'Construction_Materials_Electrical', 'Construction_Materials_Finishing', 'Construction_Materials_Plumbing', 'Art_Supplies', 'Plant_Starts', 'Seeds', 'Compost_Manure_Mulch', 'Domestic_Animals', 'Aquaponics_Hydroponics', 'Lights', 'Pots', 'Land_Agriculture', 'Land_Housing', 'Community_Space', 'Money', 'Vehicle', 'Energy_Generation']
    Tools_Construction                  = models.BooleanField(default=False)
    Tools_Farming                       = models.BooleanField(default=False)
    Tools_Art                           = models.BooleanField(default=False)
    Earthmoving_Equipment               = models.BooleanField(default=False)
    Construction_Materials_Structural   = models.BooleanField(default=False)
    Construction_Materials_Electrical   = models.BooleanField(default=False)
    Construction_Materials_Finishing    = models.BooleanField(default=False)
    Construction_Materials_Plumbing     = models.BooleanField(default=False)
    Art_Supplies                        = models.BooleanField(default=False)
    Plant_Starts                        = models.BooleanField(default=False)
    Seeds                               = models.BooleanField(default=False)
    Compost_Manure_Mulch                = models.BooleanField(default=False)
    Domestic_Animals                    = models.BooleanField(default=False)
    Aquaponics_Hydroponics              = models.BooleanField(default=False)
    Lights                              = models.BooleanField(default=False)
    Pots                                = models.BooleanField(default=False)
    Land_Agriculture                    = models.BooleanField(default=False)
    Land_Housing                        = models.BooleanField(default=False)
    Community_Space                     = models.BooleanField(default=False)
    Money                               = models.BooleanField(default=False)
    Vehicle                             = models.BooleanField(default=False)
    Energy_Generation                   = models.BooleanField(default=False)

    SKILLS = ['Teaching','Green_Building', 'Construction', 'Site_Planning', 'Gardening', 'Energy_Installation', 'Aquaponics_Hydroponics', 'Composting', 'Local_Ecology_Knowledge', 'Animal_Husbandry', 'Automotive_Maintenance', 'Herbal_Medicine', 'Bodywork_Breathwork', 'Acupuncture', 'Sound_Healing', 'Music', 'Painting', 'Sculpture', 'Dance_Performance', 'Cooking', 'Children_Programs', 'Planning_Coordination', 'Disruptive_Action', 'Facilitation', 'Local_Community_Knowledge', 'Grant_Writing', 'Digital_Media', 'Web_Development', 'Journalism', 'Promoting', 'Audio_Video_Engineering', 'Legal_Regulations', 'Legal_Defense', 'Manual_Labor', 'Photography']
    Teaching                    = models.BooleanField(default=False)
    Green_Building              = models.BooleanField(default=False)
    Construction                = models.BooleanField(default=False)
    Site_Planning               = models.BooleanField(default=False)
    Gardening                   = models.BooleanField(default=False)
    Energy_Installation         = models.BooleanField(default=False)
    Aquaponics_Hydroponics      = models.BooleanField(default=False)
    Composting                  = models.BooleanField(default=False)
    Local_Ecology_Knowledge     = models.BooleanField(default=False)
    Animal_Husbandry            = models.BooleanField(default=False)
    Automotive_Maintenance      = models.BooleanField(default=False)
    Herbal_Medicine             = models.BooleanField(default=False)
    Bodywork_Breathwork         = models.BooleanField(default=False)
    Acupuncture                 = models.BooleanField(default=False)
    Sound_Healing               = models.BooleanField(default=False)
    Music                       = models.BooleanField(default=False)
    Painting                    = models.BooleanField(default=False)
    Sculpture                   = models.BooleanField(default=False)
    Dance_Performance           = models.BooleanField(default=False)
    Cooking                     = models.BooleanField(default=False)
    Children_Programs           = models.BooleanField(default=False)
    Planning_Coordination       = models.BooleanField(default=False)
    Disruptive_Action           = models.BooleanField(default=False)
    Facilitation                = models.BooleanField(default=False)
    Local_Community_Knowledge   = models.BooleanField(default=False)
    Grant_Writing               = models.BooleanField(default=False)
    Digital_Media               = models.BooleanField(default=False)
    Web_Development             = models.BooleanField(default=False)
    Journalism                  = models.BooleanField(default=False)
    Promoting                   = models.BooleanField(default=False)
    Audio_Video_Engineering     = models.BooleanField(default=False)
    Legal_Regulations           = models.BooleanField(default=False)
    Legal_Defense               = models.BooleanField(default=False)
    Manual_Labor                = models.BooleanField(default=False)
    Photography                 = models.BooleanField(default=False)

    title        = models.CharField(max_length=200)
    summary      = models.TextField()
    collaborator = models.CharField(max_length=500)
    location     = models.CharField(max_length=200)
    seeking_help = models.CharField(max_length=1, choices=BINARY_CHOICE)    
    help_text    = models.TextField()
    ptype        = models.CharField(max_length=2, choices=TYPES)
    link         = models.CharField(max_length=300)
    connections  = models.TextField()    

    def project_type_label(self):
        pt = self.ptype
        types_dic = {'SG':'Academic',
                     'FP':'For Profit',
                     'NP':'Non Profit',
                     'GV':'Government',
                     'UC':'Unclassified',}
        ptype_label = types_dic[pt]
        return ptype_label
    def categories(self):
        cat_list = self.CATEGORIES
        p_cat_list = []
        for cat in cat_list:
            if getattr(self, cat):
                p_cat_list.append(cat)
        return p_cat_list
    def resources(self):
        res_list = self.RESOURCES
        p_res_list = []
        for res in res_list:
            if getattr(self, res):
                p_res_list.append(res)
        return p_res_list
    def skills(self):
        ski_list = self.SKILLS
        p_ski_list = []
        for ski in ski_list:
            if getattr(self, ski):
                p_ski_list.append(ski)
        return p_ski_list

    def searchblob(self):
        blob = "%s%s" % (self.title, self.summary)
        lowercaseblob = blob.lower()
        return lowercaseblob
    def __unicode__(self):
        return self.title


## Forum content
class GroupPosting(models.Model):
    groupid  = models.IntegerField()
    title    = models.CharField(max_length=300)
    content  = models.TextField()
    time     = models.DateTimeField()
    username = models.CharField(max_length=200)
    def __unicode__(self):
        s = self.title
        return s

class ProjectPosting(models.Model):
    groupid  = models.IntegerField()
    title    = models.CharField(max_length=300)
    content  = models.TextField()
    time     = models.DateTimeField()
    username = models.CharField(max_length=200)
    def __unicode__(self):
        s = self.title
        return s

class Comment(models.Model):
    top_level = models.BooleanField()
    parentid  = models.IntegerField() ##Posting if top_level, comment otherwise
    content   = models.TextField()
    time      = models.DateTimeField()
    username   = models.CharField(max_length=200)
    def __unicode__(self):
        s = self.content
        return s

class Profile(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    tagline  = models.CharField(max_length=250)
    # Picture eventually
    location = models.CharField(max_length=200)
    CATEGORIES = ['food', 'social', 'energy', 'activism', 'environment',
                  'projects', 'arts', 'education', 'policy', 'wellness', 'housing', 'research']
    food        = models.BooleanField(default=False)
    social      = models.BooleanField(default=False)
    energy      = models.BooleanField(default=False)
    activism    = models.BooleanField(default=False)
    environment = models.BooleanField(default=False)
    projects    = models.BooleanField(default=False)
    arts        = models.BooleanField(default=False)
    education   = models.BooleanField(default=False)
    policy      = models.BooleanField(default=False)
    wellness    = models.BooleanField(default=False)
    housing     = models.BooleanField(default=False)
    research    = models.BooleanField(default=False)

    RESOURCES = ['Tools_Construction', 'Tools_Farming', 'Tools_Art', 'Earthmoving_Equipment', 'Construction_Materials_Structural', 'Construction_Materials_Electrical', 'Construction_Materials_Finishing', 'Construction_Materials_Plumbing', 'Art_Supplies', 'Plant_Starts', 'Seeds', 'Compost_Manure_Mulch', 'Domestic_Animals', 'Aquaponics_Hydroponics', 'Lights', 'Pots', 'Land_Agriculture', 'Land_Housing', 'Community_Space', 'Money', 'Vehicle', 'Energy_Generation']
    Tools_Construction                  = models.BooleanField(default=False)
    Tools_Farming                       = models.BooleanField(default=False)
    Tools_Art                           = models.BooleanField(default=False)
    Earthmoving_Equipment               = models.BooleanField(default=False)
    Construction_Materials_Structural   = models.BooleanField(default=False)
    Construction_Materials_Electrical   = models.BooleanField(default=False)
    Construction_Materials_Finishing    = models.BooleanField(default=False)
    Construction_Materials_Plumbing     = models.BooleanField(default=False)
    Art_Supplies                        = models.BooleanField(default=False)
    Plant_Starts                        = models.BooleanField(default=False)
    Seeds                               = models.BooleanField(default=False)
    Compost_Manure_Mulch                = models.BooleanField(default=False)
    Domestic_Animals                    = models.BooleanField(default=False)
    Aquaponics_Hydroponics              = models.BooleanField(default=False)
    Lights                              = models.BooleanField(default=False)
    Pots                                = models.BooleanField(default=False)
    Land_Agriculture                    = models.BooleanField(default=False)
    Land_Housing                        = models.BooleanField(default=False)
    Community_Space                     = models.BooleanField(default=False)
    Money                               = models.BooleanField(default=False)
    Vehicle                             = models.BooleanField(default=False)
    Energy_Generation                   = models.BooleanField(default=False)
 
    SKILLS = ['Teaching','Green_Building', 'Construction', 'Site_Planning', 'Gardening', 'Energy_Installation', 'Aquaponics_Hydroponics', 'Composting', 'Local_Ecology_Knowledge', 'Animal_Husbandry', 'Automotive_Maintenance', 'Herbal_Medicine', 'Bodywork_Breathwork', 'Acupuncture', 'Sound_Healing', 'Music', 'Painting', 'Sculpture', 'Dance_Performance', 'Cooking', 'Children_Programs', 'Planning_Coordination', 'Disruptive_Action', 'Facilitation', 'Local_Community_Knowledge', 'Grant_Writing', 'Digital_Media', 'Web_Development', 'Journalism', 'Promoting', 'Audio_Video_Engineering', 'Legal_Regulations', 'Legal_Defense', 'Manual_Labor', 'Photography']
    Teaching                	= models.BooleanField(default=False)
    Green_Building          	= models.BooleanField(default=False)
    Construction            	= models.BooleanField(default=False)
    Site_Planning           	= models.BooleanField(default=False)
    Gardening               	= models.BooleanField(default=False)
    Energy_Installation     	= models.BooleanField(default=False)
    Aquaponics_Hydroponics  	= models.BooleanField(default=False)
    Composting                  = models.BooleanField(default=False)
    Local_Ecology_Knowledge 	= models.BooleanField(default=False)
    Animal_Husbandry        	= models.BooleanField(default=False)
    Automotive_Maintenance  	= models.BooleanField(default=False)
    Herbal_Medicine         	= models.BooleanField(default=False)
    Bodywork_Breathwork     	= models.BooleanField(default=False)
    Acupuncture             	= models.BooleanField(default=False)
    Sound_Healing           	= models.BooleanField(default=False)
    Music                   	= models.BooleanField(default=False)
    Painting                	= models.BooleanField(default=False)
    Sculpture               	= models.BooleanField(default=False)
    Dance_Performance       	= models.BooleanField(default=False)
    Cooking                 	= models.BooleanField(default=False)
    Children_Programs       	= models.BooleanField(default=False)
    Planning_Coordination   	= models.BooleanField(default=False)
    Disruptive_Action       	= models.BooleanField(default=False)
    Facilitation            	= models.BooleanField(default=False)
    Local_Community_Knowledge   = models.BooleanField(default=False)
    Grant_Writing           	= models.BooleanField(default=False)
    Digital_Media           	= models.BooleanField(default=False)
    Web_Development         	= models.BooleanField(default=False)
    Journalism              	= models.BooleanField(default=False)
    Promoting               	= models.BooleanField(default=False)
    Audio_Video_Engineering 	= models.BooleanField(default=False)
    Legal_Regulations       	= models.BooleanField(default=False)
    Legal_Defense           	= models.BooleanField(default=False)
    Manual_Labor                = models.BooleanField(default=False)
    Photography             	= models.BooleanField(default=False) 

    # events groups projects -- linkage
    other_interests = models.CharField(max_length=200)
    #other_skills = models.CharField(max_length=200)
    #other_resources = models.CharField(max_length=200)
    wdywtd = models.TextField() #What do you want to do
    needs = models.TextField()
    offerings = models.TextField()
    ideal_collaboration = models.TextField() #  NOTICE BELOW: p_ski vs g_cat
    def resources(self):
        res_list = self.RESOURCES
        p_res_list = []
        for res in res_list:
            if getattr(self, res):
                p_res_list.append(res)
        return p_res_list
    def skills(self):
        ski_list = self.SKILLS
        p_ski_list = []
        for ski in ski_list:
            if getattr(self, ski):
                p_ski_list.append(ski)
        return p_ski_list
    def categories(self):
        cat_list = self.CATEGORIES
        g_cat_list = []
        for cat in cat_list:
            if getattr(self, cat):
                g_cat_list.append(cat)
        return g_cat_list
    def __unicode__(self):
        return self.username
    def fullname(self):
        user = User.objects.filter(username=self.username)[0]
        fname = user.first_name
        lname = user.last_name
        fullname = "%s %s" % (fname, lname)
        return fullname
    def firstname(self):
        user = User.objects.filter(username=self.username)[0]
        fname = user.first_name
        return fname
## Sectors:
# government
# business
# nonprofit
# academic
# unclassified
#  
