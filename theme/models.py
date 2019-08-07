from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User , Group

# Create your models here.

class Theme(models.Model):
    # 테마_제목
    title = models.CharField(max_length=200)
    # 테마_게시자
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="theme_author")
    # 테마_템플릿파일명
    template_nm = models.TextField(max_length=1000)

    # 생성 일자
    create_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정자 
    last_modified_user_id = models.ForeignKey(User , on_delete=models.CASCADE , related_name="last_modified_user")

