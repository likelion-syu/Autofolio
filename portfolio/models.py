from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User , Group

# 드래프트 모델을 불러옴
from draft.models import Draft

# 실제 생성된 포트폴리오
#  : 본 테이블의 내용은 실제 홈페이지 개설 정보와 일치함
class Portfolio(models.Model):
    # 포트폴리오_제목
    title = models.CharField(max_length=200)
    # 생성 일자
    created_dt = models.DateTimeField(default=timezone.now)
    
    # 포트폴리오와 연결된 드래프트의 아이디
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE)
    # 포트폴리오와 연결된 theme 아이디도 필요함 

    # 사용여부 
    # 1 : 사용함 0 : 사용 안함 
    use_yn = models.SmallIntegerField(default=1)
    # 최종 수정 일자
    last_modified_dt = models.DateTimeField(default = timezone.now)
    # 최종 수정자 번호 
    last_modified_user=  models.ForeignKey(User , on_delete=models.CASCADE)

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

