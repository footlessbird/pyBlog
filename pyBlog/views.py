from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post


# 'pyBlog/home.html' 처럼 pyBlog path정해주면 에러발생! 알아서 default로 templates디렉토리에 내에 있다고 설정되 있는 듯

# function based view
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'pyBlog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # context 딕셔너리 내 'posts'
    ordering = ['-date_posted']  # 최신 게시글이 상단에 위치
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'pyBlog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # context 딕셔너리 내 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') # 최신 게시글 순으로 정렬


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'pyBlog/about.html', {'title': 'About'})
