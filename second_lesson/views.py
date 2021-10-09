from django.shortcuts import render


def index(request):
    name = 'Учиха Марлен'
    return render(request, 'index.html', locals())

def index2(request):
    name = 'Учиха Чопа'
    return render(request, 'index2.html', locals())

def index3(request):
    name = 'Чопа'
    return render(request, 'index2.html', locals())

def index4(request):
    name = 'Хук Буча'
    return render(request, 'index2.html', locals())

def index5(request):
    name = 'Дарова Заебал'
    return render(request, 'index2.html', locals())