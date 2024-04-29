from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def hola(request):
    return HttpResponse("hola,cracks")

def registro(request):
    if request.method == 'GET': 
     return render(request, 'registro.html', {'form':
        UserCreationForm})
    else:  
     if request.POST['password1'] == request.POST['password2']:
        try: 
         user = User.objects.create(username = request.POST['username'], 
                                    password = request.POST['password1'])
         user.save()
        #  if request.POST['username'] == 'perez' and request.POST['password1'] == 123:
        #      redirect('hi')
        #  else:
        #      return HttpResponse('hola')
         return redirect('hi')
        except: 
          return render(request, 'registro.html', {'form':
          UserCreationForm, 'error':'your user already exists'})
     else:
         return render(request, 'registro.html', {'form':
         UserCreationForm, 'error':'your password do not match'})


# Create your views here.
