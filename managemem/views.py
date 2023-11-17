from django.shortcuts import render
from managemem.models import Member
from django.http import HttpResponseRedirect


# Create your views here.
#Home
def home(request):
    all_members = Member.objects.all()
    return render(request, 'home.html', {"members": all_members})

#Add
def add_member(request):
    if request.method == "POST":
        if request.POST.get('lastname') \
            and request.POST.get('firstname') \
            and request.POST.get('date') \
            and request.POST.get('contract_duration') \
            and request.POST.get('group') \
            or request.POST.get('gender'):
            member = Member()
            member.lastname = request.POST.get('lastname')
            member.firstname = request.POST.get('firstname')
            member.group = request.POST.get('group')
            member.date = request.POST.get('date')
            member.contract_duration = request.POST.get('contract_duration')
            member.gender = request.POST.get('gender')
            member.save()
            return HttpResponseRedirect('/')
    else:
            return render(request, 'add.html')
    
#View
def member(request, member_id):
    member = Member.objects.get(id = member_id)
    if member != None:
        return render(request, 'edit.html', {'member': member})

#Edit
def edit_member(request):
     if request.method == "POST":
            member = Member.objects.get(id=request.POST.get('id'))
            if member is not None:
                member.lastname = request.POST.get('lastname')
                member.firstname = request.POST.get('firstname')
                member.group = request.POST.get('group')
                member.date = request.POST.get('date')
                member.contract_duration = request.POST.get('contract_duration')
                member.gender = request.POST.get('gender')
                member.save()
                return HttpResponseRedirect('/')

#Delete
def delete_member(request, member_id):
     member = Member.objects.get(id = member_id)
     member.delete()
     return HttpResponseRedirect('/')