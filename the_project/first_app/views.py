# from django.shortcuts import render
from django.http import HttpResponse
# .models means find models.py in same directory
from .models import Members

# Create your views here.


def index(request):
    members = Members.objects.all()
    # members = Members.objects.all()[1:3] # offset 1 (start from second record), return 3 rows
    # .get returns a single row, .all returns an array
    output = ', '.join([member.name for member in members])
    return HttpResponse(output)


def home(request):
    return HttpResponse('home')


def cost(request):
    return HttpResponse('cost')


def add_member(request):
    member = Members(name='Harry')
    member.save()
    return HttpResponse('created')


def update_member(request):
    member = Members.objects.get(name='Harry')
    member.name = 'HARRY'
    member.save()
    return HttpResponse('updated')


def del_member(request):
    member = Members.objects.filter(name='HARRY')
    member.delete()
    return HttpResponse('deleted')