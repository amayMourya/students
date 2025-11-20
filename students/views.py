from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentRegistrationForm, StudentProfileForm, UserUpdateForm
from .models import Student

def home(request):
    """Home page view"""
    return render(request, 'students/home.html')

def register(request):
    """Student registration view"""
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        profile_form = StudentProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Save user
            user = user_form.save()
            
            # Save student profile
            student = profile_form.save(commit=False)
            student.user = user
            student.save()
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        user_form = StudentRegistrationForm()
        profile_form = StudentProfileForm()
    
    return render(request, 'students/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def user_login(request):
    """User login view"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'students/login.html', {'form': form})

@login_required
def profile(request):
    """Show student profile"""
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('home')
    
    return render(request, 'students/profile.html', {'student': student})

@login_required
def update_profile(request):
    """Update student profile"""
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('home')
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=student)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = StudentProfileForm(instance=student)
    
    return render(request, 'students/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')

def exit_app(request):
    """Exit application view"""
    return render(request, 'students/exit.html')