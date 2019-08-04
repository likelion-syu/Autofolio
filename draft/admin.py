from django.contrib import admin
from .models import Draft, DraftActivity , DraftPortfolio, DraftResume
# Register your models here.

admin.site.register(Draft)
admin.site.register(DraftActivity)
admin.site.register(DraftPortfolio)
admin.site.register(DraftResume)
