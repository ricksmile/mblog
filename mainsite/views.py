#coding=utf-8
from django.template.loader import get_template
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from datetime import datetime
from .models import Post
from .models import Product
import random


# Create your views here.
def homepage(request):
	template = get_template('index.html')
	quotes=['諸行無常','諸法無我','寂滅涅槃']
	html=template.render({'quote':random.choice(quotes)})
	return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
		
def disp_detail(request,sku):
	try:
		p=Product.objects.get(sku=sku)
	except Product.DoesNoExist:
		raise Http404('can not find')
	template=get_template('disp.html')	
	
	
	html=template.render({'product':p})
	
	return HttpResponse(html)
  
      


  
  
def about(request):
  html='''
  <!DOCTYPE html>
  <html>
  <head>  
  <title>
   !!@@@@
  </title>
  </head>
  <body>
  <h2>
  Ricksmile
  </h2>
  </body>
  </html>
  '''
  return  HttpResponse(html)
  
def listing(request):
 
  products=Product.objects.all()
  template=get_template('list.html')
  html=template.render({'products':products})
  return  HttpResponse(html)
  
  
  
  
  
  
  
  