from django.shortcuts import render
from .models import Post


# 'pyBlog/home.html' 처럼 pyBlog path정해주면 에러발생! 알아서 default로 templates디렉토리에 내에 있다고 설정되 있는 듯
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})
