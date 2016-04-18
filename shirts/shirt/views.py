from django.shortcuts import render
from .models import Product, Product_Varients, Sno
from .forms import ChoiceForm
# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template import Template , Context
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404


def some_view(request):
	choices_picked = []
	if request.method == 'POST':
		form = ChoiceForm(request.POST)
		if form.is_valid():
			choices_picked = form.cleaned_data.get('choices_picked')
			# do something with your results
			
			print choices_picked
	else:
		form = ChoiceForm


	queryset_list = []
	if len(choices_picked) == 0:
		queryset_list = Product.objects.all()
	else:
		for i in choices_picked:
			a = Product_Varients.objects.filter(size=i)
			print a
			for j in a:
				queryset_list.extend(Product.objects.filter(product_id=j.product_id))



	#queryset_list = Product.objects.all()
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)



	context = {
		"form": form,
		"page_request_var": page_request_var,
		"object_list": queryset,
	}
	return render(request ,'base.html', context)