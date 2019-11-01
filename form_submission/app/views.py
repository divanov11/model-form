from django.shortcuts import render
from .forms import CustomerForm


def index(request):

	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'app/index.html', context)