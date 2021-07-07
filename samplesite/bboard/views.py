from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Bb


def index(request):
    # template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    # context = {'bbs': bbs}
    # s = 'Список объявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return render(request, 'bboard/index.html', {'bbs': bbs})