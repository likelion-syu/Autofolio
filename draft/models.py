from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User , Group

# 파일 저장 관련 주소생성 함수 
def directory_path_by_user(instance , filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = timezone.now()
    return '{0}/user_{1}/{2}'.format(now.strftime('%Y%m') , instance.user_id.id , filename)

# 드래프트 전체를 관리하는 모델
class Draft(models.Model):
    # 드래프트 제목
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="draft_author")

    # 드래프트 생성일
    created_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정자
    last_modified_user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="draft_last_modified_user")
    
# 드래프트 중 이력서 항목 관리용 모델
class DraftResume(models.Model):
    # 관련 드래프트 번호
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE , default=None)
    # 이력서_이름 
    name = models.CharField(max_length=50)
    # 이력서_나이
    age = models.IntegerField()

    # 생성 일자
    created_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정자
    last_modified_user= models.ForeignKey(User, on_delete=models.CASCADE)

# 드래프트 중 포트폴리오 항목 관리용 모델
class DraftPortfolio(models.Model):
    # 관련 드래프트 번호 
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE )
    # 포트폴리오_제목
    title = models.CharField(max_length=200)
    # 포트폴리오_내용
    desc = models.TextField(max_length=2000)
    
    # 포트폴리오 타입 
    # 0 : links , 1 : files , 2 : videos
    portfolio_type = models.IntegerField()
    # 포트폴리오_첨부 링크 
    attached_link = models.TextField(blank=True , max_length=1000)
    # 포트폴리오_첨부 파일
    attached_file = models.FileField(blank=True , upload_to=directory_path_by_user)
    # 포트폴리오_비디오 태그 : 유튜브 형태 
    attached_video_tag = models.TextField(blank=True , max_length=1000)

    # 생성 일자
    created_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정자
    last_modified_user = models.ForeignKey(User, on_delete=models.CASCADE)

# 드래프트 중 활동 내역 항목 관리용 모델
class DraftActivity(models.Model):
    # 관련 드래프트 번호
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE)
    # 활동내역_제목
    title = models.CharField(max_length=200)
    # 활동내역_내용
    desc = models.TextField(max_length=2000)
    # 활동내역_활동 일자
    activity_dt = models.DateField()

    # 생성 일자
    created_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정일자 
    last_modified_dt = models.DateTimeField(default=timezone.now)
    # 최종 수정자
    last_modified_user = models.ForeignKey(User , on_delete = models.CASCADE)


