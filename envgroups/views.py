from django.shortcuts import render
from models import Group, Event

# Create your views here.
def index(request):
    return render(request, 'envgroups/index.html')


