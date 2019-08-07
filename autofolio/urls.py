from django.contrib import admin
from django.urls import path , include
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.index , name="main"),
    path('account/' , include('account.urls')),
    path('portfolio/' , include('portfolio.urls')),
    path('draft/' , include('draft.urls')),
<<<<<<< HEAD
    path('theme/', include('theme.urls')),
=======
    path('theme/', include('theme.urls'))
>>>>>>> e9db5751b24b5609bbca1ae30b4f2b6f8dc2921a
]

# 업로드된 이미지를 가져오기 위한 url 설정
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
