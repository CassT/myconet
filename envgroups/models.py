from django.db import models

# Environmental Groups and Events
class Group(models.Model):
    # Need to add picture upload somewhere
    CATEGORIES = (
        ('FO','Food'),
        ('SO','Social'),
        ('EN','Energy'),
        ('AC','Activism'),
        ('EV','Environment'),
        ('PR','Projects'),
        ('AR','Arts'),
        ('ED','Education'),
        ('PO','Policy'), 
    )
    BINARY_CHOICE = (
        ('Y','Yes'),
        ('N','No'),
    )
    TYPES = (
        ('SG','Student Group'),
        ('FP','For Profit'),
        ('NP','Non Profit'),
    )
#    category    = models.CharField(max_length=2, choices=CATEGORIES)
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
    def __unicode__(self):
        return self.title

class Event(models.Model):
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
    def __unicode__(self):
        s = self.time.strftime('%Y-%m-%d %H:%M ') + self.name
        return s

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

class Comment(models.Model):
    top_level = models.BooleanField()
    parentid  = models.IntegerField() ##Posting if top_level, comment otherwise
    content   = models.TextField()
    time      = models.DateTimeField()
    username   = models.CharField(max_length=200)
    def __unicode__(self):
        s = self.content
        return s

