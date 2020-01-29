from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import *
# Create your views here.

def user_create(request):
    if request.method == 'POST':
        json_data = request.POST
        user = Users()
        for k, v in json_data.items():
            setattr(user, key, value)
        user.save()
        return JsonResponse(model_to_dict(userObj))
    else:
        return HttpResponse("error")

def user_info(request, user_id):
    if request.method == 'POST':
        json_data = request.POST
        user = Users.objects.get(pk=user_id)
        if 'username' in json_data:
            user.username = json_data['username']
        if 'email' in json_data:
            user.email = json_data['email']
        if 'location' in json_data:
            user.location = json_data['location']
        user.save()
        return JsonResponse(model_to_dict(user)) 
    else:
        return HttpResponse("error")

def user_all(request):
    if request.method == 'GET':
        users = Users.objects.all()
        usersList = []
        for i in users:
            usersList.append(model_to_dict(i))
        return JsonResponse(usersList, safe=False)
    else:
        return HttpResponse("error")

def send_json(request):

    data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]

    return HttpResponse("error")