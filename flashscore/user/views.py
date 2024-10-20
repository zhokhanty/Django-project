from .models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('home')
        else:
            context['error'] = True
    return render(request, 'user/login.html')

@login_required
def logout_view(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect('home')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        errors = []

        if not username or not email or not password or not password_confirm:
            errors.append("All fields are required.")
        if password != password_confirm:
            errors.append("Passwords do not match.")
        try:
            validate_password(password)
        except ValidationError as e:
            errors.extend(e.messages)
        if Profile.objects.filter(username=username).exists():
            errors.append("Username already taken.")
        if Profile.objects.filter(email=email).exists():
            errors.append("Email already taken.")

        if not errors:
            user = Profile.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            Profile.objects.create(user=user)

            login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/register.html', {'errors': errors})

    return render(request, 'user/register.html')