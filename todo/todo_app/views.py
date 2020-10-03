from django.shortcuts import render, redirect
from todo_app.models import List
from todo_app.forms import ListForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
def about(request):
    return render(request,"todo_app/about.html")

def home(request):
    form = ListForm
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            item = List.objects.all()
            d1 = List.objects.last()
            messages.success(request,str(d1)+"has been added")
            return render(request,"todo_app/home.html",{'item':item})
    item = List.objects.all()
    return render(request,"todo_app/home.html",{'item':item})

def remove(request,pk):
    item = List.objects.get(pk=pk)
    item.delete()
    messages.success(request,"{} has been deleted".format(item.item))
    return redirect('todo_app:home')

def cross(request,pk):
    completed = List.objects.get(pk=pk)
    completed.completed = True
    completed.save()
    return redirect('todo_app:home')


def uncross(request,pk):
    completed = List.objects.get(pk=pk)
    completed.completed = False
    completed.save()
    return redirect('todo_app:home')

def edit(request,pk):
    if request.method=="POST":
        item = List.objects.get(pk=pk)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,"{} has been edited".format(item))
            return redirect('todo_app:home')
    else:
        item = List.objects.get(pk=pk)
        return render(request,'todo_app/edit.html',{'item':item})
