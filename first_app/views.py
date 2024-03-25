from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic
from . import forms

def index(request):
   names=Topic.objects.all()
   my_dict={'access_records':names}
   return render(request,'first_app/index.html',context=my_dict)

def form_name_view(request):
   form=forms.FormName()

   if request.method=='POST': 
      form=forms.FormName(request.POST)

      if form.is_valid():
         print("Validation Success")
         print(form.cleaned_data['name'])
         print(form.cleaned_data['email'])
         print(form.cleaned_data['text'])



   return render(request,'first_app/form_page.html',{'form':form})


# Create your views here.
