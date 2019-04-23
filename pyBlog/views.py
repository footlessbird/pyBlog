from django.shortcuts import render

posts = [
    {
        'author': 'Shazam',
        'title': 'Shaaaaaaaazam!!!!!',
        'content': 'power overwhelming',
        'date_posted': 'April 22, 2019'

    },
    {
        'author': 'Batman',
        'title': 'The Dark Knight',
        'content': 'I am not Bruce Wayne',
        'date_posted': 'April 21, 2019'

    },
]


# 'pyBlog/home.html' 처럼 pyBlog path정해주면 에러발생! 알아서 default로 templates디렉토리에 내에 있다고 설정되 있는 듯
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title':'About'})
