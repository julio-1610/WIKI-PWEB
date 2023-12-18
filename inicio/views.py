from django.shortcuts import render

# Create your views here.
def myHome(request, *args, **kwargs):
  return render(request, 'home.html',{})
