from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from play.models import MatchMeking

User = get_user_model()

@api_view(['GET','POST'])
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
    else:
        return render(request, 'accounts/signup.html')

@api_view(['GET', 'POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'accounts/login.html')

def logout_user(request):
    user_id = request.session.get('user_id')
    
    existing_match = MatchMeking.objects.filter(id_user=user_id).first()
    if existing_match:
        existing_match.delete()
    logout(request)

    return redirect('index')

@api_view(['GET'])
def getData(request):
    app = Player.objects.all()
    serializer = PlayerSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)