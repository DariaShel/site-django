from django.shortcuts import render
from blog.models import DashaPost
from django.utils import timezone
# Create your views here.

def BlogList(request):
	posts = DashaPost.objects.all()
	args = {}
	args['posts'] = posts
	return render(request,'myblog.html',args)

def BlogSend(request):
	if request.method == "POST":
		title = request.POST.get('title', '')
		body = request.POST.get('body', '')
		p = DashaPost()
		p.title = title
		p.body = body
		p.timestamp = timezone.now()
		p.save()

	return BlogList(request)

def BlogDel(request, id):
	d = DashaPost.objects.get(id=id)
	d.delete()

	return BlogList(request)