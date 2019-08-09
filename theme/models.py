from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User , Group

# 파일 저장 관련 주소생성 함수 
def directory_path_by_user(instance , filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = timezone.now()
    return '{0}/user_{1}/{2}'.format(now.strftime('%Y%m') , instance.author.id , filename)


class Theme(models.Model):
    # 테마_제목
    title = models.CharField(max_length=200)
    # 테마_게시자
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="theme_author")
    # 테마_템플릿파일명
    template_nm = models.TextField(max_length=1000)

    thumbnail = models.ImageField(upload_to=directory_path_by_user , default="1234")

    # 생성 일자
    create_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정자 
    last_modified_user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="theme_last_modified_user")

