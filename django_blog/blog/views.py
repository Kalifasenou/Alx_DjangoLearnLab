from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automatique après inscription
            return redirect('post-list')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        # simple exemple : changer email
        request.user.email = request.POST.get('email', request.user.email)
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html')
