from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect


# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello world</h1>')
    return HttpResponsePermanentRedirect('/home')


def about(request):
    return HttpResponse('<b>О нашей фирме</b>')


def home(req):
    return render(req, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def workers(req):
    return render(req, 'workers.html')


def month(req, id):
    id = int(id)
    month = ['март', 'апрель', 'май']
    workers = ['Иван', 'Петр', 'Джон']
    imgs = ['img/1.jpg', 'img/2.jpg', 'img/3.jpg']
    data = {'k1': month[id], 'k2': workers[id], 'k3': imgs[id]}
    return render(req, 'month.html', context=data)


def product(req, id):
    id = int(id)
    name = ['Креветка', 'Осьминог', 'Акула']
    imgs = ['img/4.png', 'img/5.jpg', 'img/6.jpg']
    data = {'k1': name[id], 'k2': imgs[id]}
    return render(req, 'product.html', context=data)


def spisok(req):
    # firmsall = ['apple', 'ibm', 'microsoft', 'oracle', 'amigo']
    firmsall = []
    data = {'firms': firmsall}
    return render(req, 'spisok.html', context=data)


def proverka(req, year):
    year=int(year)
    data = {'year':  year}
    return render(req, 'proverka.html', context=data)
