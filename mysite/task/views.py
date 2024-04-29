from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#UserCreationForm: esta funcion nos permitira utilizar el registro que viene por defecto en django
#AuthenticationForm: esta funcion nos permitira utilizar el inicio de sesion que viene por defecto en django
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')

def hola(request):
    return HttpResponse('<h1> hola </h1>')

def sign_up(request):
    #  esta condicion se va a cumplir si el usario tan solo va a presenciar el despliegue de la interfaz
    if request.method == 'GET':
        print('enviando datos')
        return render(request, 'sign_up.html', {'form':
        UserCreationForm})
    #hacemos mencion de la funcion 'UserCreationForm' en el render para que posteriormente 
    # lo interprete el navegador como un html
    else:
    #    esta condicion se va a cumplir al momento de que el usuario ingrese sus datos en la casilla de texto. esto sucede por el tipo
    # de request implementado
     if request.POST['password1'] == request.POST['password2']:
        try:
             user = User.objects.create(username = request.POST['username'], 
                                        password = request.POST['password1'])
             #tomamos la funcion 'User' para insertar los datos ingresados en los labels a la bd y por consecuenta crear su usuario en el proyecto
             user.save()
            #esta funcion guarda los datos ingresado en la variable 'user' y los inserta en la bd
             login(request, user)
            #  esta funcion nos permitira crear un cookie del usuario una vez se registre en el proyecto. 
            #  una cookie identifica tu usuario o computadora al momento en que te registras en una pagina web, con el
            #  fin de tener un registro de todos tus movimientos en dicha pagina. Aquellos movimientos como los datos que ingresas al
            #  momento de registrarte
            #  print(request.POST)
            #  print('obteniendo dateros')
            #  return HttpResponse('your user has been successfully')
             return redirect('signinn')
         #nos redireccioname al nombre de una url
        except IntegrityError: #este error simboliza una falla en la integridad del registro, es decir, hacer caso omiso a los parametro impuestos al mismo
         return render(request, 'sign_up.html', {'form':
           UserCreationForm, 'error':'your user already exists'})
     else:
        return render(request, 'sign_up.html', {'form':
           UserCreationForm, 'error':'password do not match'})
    
def tasks(request):
    return render(request, 'task.html')

def cerrar_sesion(request):
    logout(request)
    #esta funcion cierra sesion automaticamente. podemos comprobar esto en el cookies generado al momento registrarse, dado que 
    # este se elimina una vez aplicamos la vista en la que se encuentra dicha funcion 
    return redirect('home')

def inicio_sesion(request): 
    if request.method == 'GET':
        return render(request, 'sign_in.html', {'form':
            AuthenticationForm  
        })
    elif request.method == 'POST':

        user = authenticate(request, username = request.POST['username'],
                                     password = request.POST['password'])
        if user is not None:
         login(request, user)
         return redirect('home')
       
        else:
         return render(request, 'sign_in.html', {'form': AuthenticationForm,
                                                 'error': 'Username or password is incorrect'})
    
    # if request.method == 'GET':
    #   return render(request, 'sign_in.html', {'form': AuthenticationForm})
 
    # else:
    #     user = authenticate(request, 
    #                      username = request.POST['username'],
    #                      password = request.POST['password'])

    #     if user is None:
    #         return render(request, 'sign_in.html', 
    #                  {'form': AuthenticationForm,
    #                  'error':'username or password is incorrect'})
    #     else:
    #         login(request, user)
    #         return redirect('home')