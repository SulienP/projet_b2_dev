from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializer import PlayerSerializer  
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

        user = authenticate(request, username=username, password=password)  # Correction de l'appel à authenticate
        if user:
            login(request, user)
            request.session['user_id'] = user.id
        
        return redirect('index')  
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