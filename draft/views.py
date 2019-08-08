from django.shortcuts import render, get_object_or_404, redirect
from .models import Draft, DraftActivity, DraftPortfolio, DraftResume

##CREATE
# new
def draft_new(req):
    return render(req,'draft/new.html')
#create
def draft_create(req):
    draft = Draft()                 ##### ㅠㅠㅠㅠ나중에 내용 추가하겟슴..
    return redirect('/draft/' + str(draft.id))

##READ
# list
def draft_list(req):
    drafts = Draft.objects.all().order_by('-id')    # 글을 최신순으로 나열
    return render(req , './draft/list.html', {'drafts':drafts})
# detail
def draft_detail(req, draft_id):
    draft_detail = get_object_or_404(Draft, pk=draft_id)
    return render(req , './draft/detail.html', {'draft':draft_detail})
##UPDATE
# edit
def draft_edit(req, draft_id):
    draft = get_object_or_404(Draft, pk=draft_id)
    return render(req, './draft/edit.html', {'draft':draft})
# update
def draft_update(req, draft_id):
    draft = get_object_or_404(Draft, pk=draft_id)       ##### draft_create 내용 추가와 같음
    return redirect('/draft/' + str(draft.id))

##DELETE
# delete
def draft_delete(req, draft_id):
    draft = get_object_or_404(Draft, pk=draft_id)
    draft.delete()
    return redirect('draft_list')
