from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django import template
from django.template import loader
import requests

from play.models import MatchMeking

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        api_url = "http://localhost:8000/api/auth/login/"  
        payload = {'username': username, 'password': password}
        response = requests.post(api_url, data=payload)

        if response.status_code == 200:  
            user_data = response.json()  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['user_id'] = user_data['id']  
                return redirect('index')  
            else:
                return JsonResponse({'message': 'Authentication successful, but failed to login locally'}, status=400)
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
    elif request.method == "GET":
        return render(request, "accounts/login.html")
    else:
        return JsonResponse({'message': 'Invalid method'}, status=405)

def logout_user(request):
    user_id = request.session.get('user_id')
    
    existing_match = MatchMeking.objects.filter(id_user=user_id).first()
    if existing_match :
        existing_match.delete()
    logout(request)

    return redirect('index')
