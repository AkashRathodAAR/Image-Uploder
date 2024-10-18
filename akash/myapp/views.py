from django.shortcuts import render
from. forms import ImageForm
from.models import Image
# Create your views here.
def home(request):
    fm=ImageForm()
    img=Image.objects.all()
    textview={
        'form':fm,
        'img':img
    }
    if  request.method=='POST':
        fm=ImageForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
        

    return render(request, 'myapp/home.html',textview)
