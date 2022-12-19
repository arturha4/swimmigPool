from django.contrib.auth import authenticate
from authentication.forms import *


def create_user(request):
    data = request.POST
    email = data['email']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    user = MyCustomUser.objects.create_user(email, password, first_name, last_name)
    return user


def auth_user(request):
    username = request.POST['email']
    password = request.POST['password']
    return authenticate(request, username=username, password=password)
