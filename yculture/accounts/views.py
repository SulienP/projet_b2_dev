from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from .edit_accounts import EditProfilPhoto

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

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            request.session['user_id'] = user.id
        
        return redirect('index')  
    return render(request, 'accounts/login.html')


def logout_user(request):
    user_id = request.session.get('user_id')
    
    existing_match = MatchMeking.objects.filter(id_user=user_id).first()
    if existing_match :
        existing_match.delete()
    logout(request)

    return redirect('index')


def settings_user(request):
    if request.method == 'POST':
        form = EditProfilPhoto(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = EditProfilPhoto(instance=request.user)

    context = { 'form': form }

    return render(request, 'accounts/settings.html', context)
