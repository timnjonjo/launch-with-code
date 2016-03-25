from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms  import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)
def about(request):
	context ={}
	template = 'aboutus.html'
	return render (request, template, context)


def login(request):
	context = {}
	context.update(csrf(request))
	return render_to_response ('login.html', context)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate (username =username, password= password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect( '/accounts/loggedin')
	else:
		return HttpResponseRedirect ('/accounts/login')

def loggedin(request):
	return render_to_response ('loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')



def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid(): 
            form.save() 


            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user=User.objects.get(username = username)                                                             
            return HttpResponseRedirect('/accounts/register_success/')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('register.html', args)

# def register_user(request):
#     args = {}
#     args.update(csrf(request))


#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/accounts/register_success')

#     return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')