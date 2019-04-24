from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # CASCADE - 회원탈퇴 시 회원의 게시글, 프사 삭제
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # 프로필을 좀 더 디테일하게 만듦
    def __str__(self):
        return f'{self.user.username} Profile'
