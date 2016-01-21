from django.db import models

# Environmental Groups and Events
class Group(models.Model):
    # Need to add picture upload somewhere
    CATEGORIES = (
        ('F','Food'),
        ('S','Social'),
        ('E','Energy'),
        ('A','Activism')
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
    category    = models.CharField(max_length=1, choices=CATEGORIES)
    title       = models.CharField(max_length=200)
    mission     = models.TextField()
    employees   = models.TextField()
    location    = models.CharField(max_length=200)
    products    = models.TextField()
    hiring      = models.CharField(max_length=1, choices=BINARY_CHOICE)
    hiring_text = models.TextField()
    gtype       = models.CharField(max_length=1, choices=TYPES)
    link        = models.CharField(max_length=300)
    connections = models.TextField()

class Event(models.Model):
    name        = models.CharField(max_length=200)
    time        = models.DateTimeField()
    location    = models.TextField()
    description = models.TextField()
    link        = models.CharField(max_length=300)
