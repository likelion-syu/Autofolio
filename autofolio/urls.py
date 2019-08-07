from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('draft/', include('draft.urls')),
=======
from django.urls import path , include
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.index , name="main"),
    path('account/' , include('account.urls')),
    path('portfolio/' , include('portfolio.urls')),
    path('draft/' , include('draft.urls')),
    path('theme/', include('theme.urls'))
>>>>>>> d360ac2e76473f663c2c05c35b60b8a78cd14e17
]

# 업로드된 이미지를 가져오기 위한 url 설정
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
