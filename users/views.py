from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # DB에 신규회원 저장
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required # user 가 반드시 로그인 되있어야 페이지 확인 가능
def profile(request):
    return render(request, 'profile.html')