from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms


#вывод не полной информации
def tv_showview(request):
    show = models.TVShow.objects.all()
    return render(request, 'tvshow.html', {'show': show})


#вывод полной информации по id
def tv_show_detailview(request, id):
    show_id = get_object_or_404(models.TVShow, id=id)
    return render(request, 'tvshow_detail.html', {'show_id': show_id})


#Добавление фильма через формы
def create_tv_show_view(request):
    method = request.method
    if method == 'POST':
        form = forms.TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Фильм успешно добавлен!!!</h2>')

    else:
        form = forms.TvShowForm()

    return render(request, 'add_tvshow.html', {'form': form})


def update_tv_show_view(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    if request.method == 'POST':
        form = forms.TvShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Фильм успешно обновлен!</h2>')
    else:
        form = forms.TvShowForm(instance=show_object)

    return render(request, 'update_tv_show.html', {
                                                    'form': form,
                                                    'object': show_object
                                                   })


def delete_tv_show_view(request, id):
    show_object = get_object_or_404(models.TVShow, id=id)
    show_object.delete()
    return HttpResponse('<h2>Фильм успешно удален</h2>')