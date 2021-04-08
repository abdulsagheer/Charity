from django.shortcuts import render
from .models import Donator
from .forms import DonateModelForm


# Create your views here.
def index(request):
    return render(request,'checkout.html')

def home(request):
    return render(request,'index.html')

def info(request):
    obj=Donator.objects.all()
    form=DonateModelForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            instance=form.save(commit=False)
            instance.name=form.cleaned_data.get('name')
            instance.email=form.cleaned_data.get('email')
            form.save()
    context={'form':form,'obj':obj}

    return render(request,'info.html',context)

