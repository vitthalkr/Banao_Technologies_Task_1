from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserSignupForm, UserLoginForm

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if user.is_patient:
                    return redirect('patient_dashboard')
                elif user.is_doctor:
                    return redirect('doctor_dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
