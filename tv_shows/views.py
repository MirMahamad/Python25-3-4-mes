from django.shortcuts import render, get_object_or_404
from . import models


#вывод не полной информации
def tv_showview(request):
    show = models.TVShow.objects.all()
    return render(request, 'tvshow.html', {'show': show})


#вывод полной информации по id
def tv_show_detailview(request, id):
    show_id = get_object_or_404(models.TVShow, id=id)
    return render(request, 'tvshow_detail.html', {'show_id': show_id})