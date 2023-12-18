from django.shortcuts import render
from .models import Markdown
from .forms import MarkdownForm
import markdown

# Create your views here.
def markdownCreateForm(request):
  form = MarkdownForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = MarkdownForm()

  context = {      
      'form': form
      }
  return render(request, 'markdown/markdownForm.html', context)

def markdownList(request):
  objetos = Markdown.objects.all()
  context = {
      'lista': objetos,
      }
  return render(request, 'markdown/list.html', context)

def markdownView(request, nombre):
  obj = Markdown.objects.get(nombre=nombre)
  htmlText = markdown.markdown(obj.texto)
  context = {
      'nombre': nombre,
      'autor': obj.autor,
      'texto': htmlText,
      }
  return render(request, 'markdown/view.html', context)
