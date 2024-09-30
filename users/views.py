from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render

from .forms import (CustomUserChangeForm, CustomUserCreationForm,
                    UserProfileUpdateForm)


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def update_user(request):
    print(dir(request.user))
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('book_home')
    else:
        form = CustomUserChangeForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'update_user.html', context=context)


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
    # http_method_names = ['get', 'post']
