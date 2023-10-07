from django.shortcuts import render,HttpResponse
from cryptography.fernet import Fernet
from django.contrib import messages
import base64

def index(request):
    return render(request,'index.html')

# token = ''
# key = ''

def encrypt(request):
    # if not token=='' or not key=='':
    #     token = ''
    #     key = ''
    message = ''
    if request.method == 'POST':
        message1 = str(request.POST.get('message'))
        key = Fernet.generate_key()
        f = Fernet(key)
        token = f.encrypt(message1.encode())
        key = str(key)
        return render(request,'encrypt.html',{'msg':token,'key':key})
    return render(request,'encrypt.html')

def decrypt(request):
    if request.method == 'POST':
        token = request.POST['text']
        key = request.POST['key']
        f = Fernet(key)
        message = f.decrypt(token.encode())
        return render(request,'decrypt.html',{'message':message})
    else:
        return render(request,'decrypt.html')

def base64encode(request):
    if request.method == 'POST':
        message = request.POST['message']
        encoded = base64.b64encode(message.encode())
        return render(request,'base64encode.html',{'encoded':encoded})
    else:
        return HttpResponse('Error')
    
def base64decode(request):
    if request.method == 'POST':
        encoded = request.POST['encoded']
        decoded = base64.b64decode(encoded.encode())
        return render(request,'base64decode.html',{'decoded':decoded})
    else:
        return HttpResponse('Error')

# Create your views here.
