from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User , Group

# 드래프트 모델을 불러옴
from draft.models import Draft
from theme.models import Theme

# 파일 저장 관련 주소생성 함수 
def directory_path_by_user(instance , filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = timezone.now()
    return '{0}/user_{1}/{2}'.format(now.strftime('%Y%m') , instance.author.id , filename)

# 실제 생성된 포트폴리오
#  : 본 테이블의 내용은 실제 홈페이지 개설 정보와 일치함
class Portfolio(models.Model):
    # 포트폴리오_제목
    title = models.CharField(max_length=200)
    # 생성 일자
    created_dt = models.DateTimeField(default=timezone.now)
    # 작성자 
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="portfolio_author")
    
    # 포트폴리오와 연결된 드래프트의 아이디
    draft = models.ForeignKey(Draft , on_delete=models.CASCADE)
    # 포트폴리오와 연결된 theme 아이디도 필요함 
    theme = models.ForeignKey(Theme , on_delete=models.CASCADE)

    tags = models.CharField(blank=True ,max_length=1000)

    # 사용여부 
    # 1 : 사용함 0 : 사용 안함 
    use_yn = models.SmallIntegerField(default=1)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default = timezone.now)
    # 최종 수정자 번호 
    last_modified_user=  models.ForeignKey(User , on_delete=models.CASCADE , related_name="last_modified_user")

# 생성된 서브도메인 관리용
class Subdomain(models.Model):
    # 서브 도메인의 이름
    domain_nm = models.TextField(max_length=100)
    # 생성된 full url
    url = models.TextField(max_length=500)
    # 관련된 포트폴리오 번호 
    portfolio_id = models.ForeignKey(Portfolio , on_delete=models.CASCADE)

    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default = timezone.now)
    # 최종 수정자 번호 
    last_modified_user = models.ForeignKey(User , on_delete=models.CASCADE)

