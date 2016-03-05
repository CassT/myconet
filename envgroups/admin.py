from django.contrib import admin
from models import Group, Event, GroupPosting, Comment

# Register your models here.
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(GroupPosting)
admin.site.register(Comment)
