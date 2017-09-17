from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
	# this will be a get and post page.  once validated it will submit form
	return render(request, "djangosurvey/index.html")

def processform(request):
	if request.method=="GET":
		return render(request, "djangosurvey/index.html")
	elif request.method == "POST":
		name = request.POST['name'].strip()
		location = request.POST['location'].strip()
		language = request.POST['language'].strip()
		comments = request.POST['comments'].strip()
		total = request.POST['total'].strip()
		request.session['name'] = name
		request.session['location'] = location
		request.session['language'] = language
		request.session['comments'] = comments
		data = {'':''}
	# return render(request, "djangosurvey/result.html")
	return redirect("results/")

def results(request):
	
	return render(request, "djangosurvey/result.html")

def test(request):

	return HttpResponse("Hello")

	"""

	"""