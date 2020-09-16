from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse


def topic(request):
    if request.method=='POST':
        topic=request.POST['topic_name']
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        t.save()
        return HttpResponse('the given data has added into ur Topic MOdel Successfully')



    return render(request,'topic.html')


def webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic_name')
        name=request.POST.get('name')
        url=request.POST.get('url')
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        return HttpResponse('one record has addedd into Webpage Model successfully')

    return render(request,'webpage.html',context={'topics':Topic.objects.all()})



def displaytopicform(request):
    if request.method=="POST":
        topic=request.POST.get('topic_name')
        webpages=Webpage.objects.filter(topic_name=topic)
        #print(webpages)
        return render(request,'displaywebpage.html',context={'webpages':webpages})

    return render(request,'displaytopicform.html',context={'topics':Topic.objects.all()})





def updateweb(request):
    if request.method=='POST':
        name=request.POST.get('name')
        url=request.POST.get('url')
        Webpage.objects.filter(name=name).update(url=url)
        
    return render(request,'updateweb.html')




