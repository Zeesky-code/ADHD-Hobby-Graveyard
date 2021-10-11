from django.shortcuts import render,redirect

from .models import *
from .forms import *
# Create your views here.
def index(request):
    hobbies = Hobby.objects.all()

    form = HobbyForm()

    if request.method =="POST":
        form = HobbyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'hobbies': hobbies, 'form': form}
    return render(request,'hobbies/list.html', context)

def updateHobby(request, pk):
    hobby = Hobby.objects.get(id=pk)

    form = HobbyForm()
    if request.method =="POST":
        form = HobbyForm(request.POST, instance=hobby)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {'form': form}
    return render(request, 'hobbies/update_hobby.html',context)