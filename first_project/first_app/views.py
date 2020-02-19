from django.shortcuts import HttpResponse, redirect


def index(request):
    return HttpResponse("I created a fucking Django project!")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,num):
    number = num
    return HttpResponse("Placeholder to display blog"+" "+number)

def edit(request,num):
    number = num
    return HttpResponse("placeholder to edit blog"+" "+number)

def destroy(request,num):
    return redirect("/")

def delete_user(request, user_id):
    return HttpResponse("User ID has been deleted")
