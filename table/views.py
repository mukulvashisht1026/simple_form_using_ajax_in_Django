from django.shortcuts import render
from .models import tableModel
from django.http import HttpResponse
# Create your views here.
def table(request):
	obj = tableModel.objects.all()
	context= {
	'obj': obj
	}
	return render(request,'table/base.html',context)

def enter(request):
	if request.method == 'POST':
		name = request.POST['name']
		address = request.POST['address']
		dob = request.POST['dob']
		obj=tableModel.objects.create(name=name,address=address,DOB=dob)
		obj.save()
		return HttpResponse('')