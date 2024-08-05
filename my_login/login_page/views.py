from django.shortcuts import render,redirect
from .forms import CreateForm
from .models import User
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return redirect('auth')
        else:
            return render(request, 'display.html', {'error': 'Email not registered'})
    return render(request, 'display.html')
def auth_view(request):
    context = {'authenticated':None}
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            context['authenticated'] = True
        else:
            context['authenticated'] = False
    return render(request,'auth.html',context)
def createUser(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display.html')
    else:
        form = CreateForm()
    return render(request,'create.html',{'form':form})