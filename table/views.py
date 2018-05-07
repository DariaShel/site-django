from django.shortcuts import render
from table.models import DashaTable
# Create your views here.
def Table(request):
	img = DashaTable.objects.all()
	args = {}
	args['img'] = img
	return render(request,'table.html',args)