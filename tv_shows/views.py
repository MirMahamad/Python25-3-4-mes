from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

#вывод не полной информации
class TvShowView(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TVShow.objects.all()

    def get_queryset(self):
        return models.TVShow.objects.all()

# def tv_showview(request):
#     show = models.TVShow.objects.all()
#     return render(request, 'tvshow.html', {'show': show})

#вывод полной информации по id


class TvShowDetailView(generic.DetailView):
    template_name = 'tvshow_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)

# def tv_show_detailview(request, id):
#     show_id = get_object_or_404(models.TVShow, id=id)
#     return render(request, 'tvshow_detail.html', {'show_id': show_id})


#Добавление фильма через формы

class TvShowCreateView(generic.CreateView):
    template_name = 'add_tvshow.html'
    form_class = forms.TvShowForm
    queryset = models.TVShow.objects.all()
    success_url = '/tvshow/'


    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form=form)



# def create_tv_show_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2>Фильм успешно добавлен!!!</h2>')
#
#     else:
#         form = forms.TvShowForm()
#
#     return render(request, 'add_tvshow.html', {'form': form})



class TvShowUpdateView(generic.UpdateView):
    template_name = 'update_tv_show.html'
    form_class = forms.TvShowForm
    success_url = "/tvshow/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)

    def form_valid(self, form):
        return super(TvShowUpdateView, self).form_valid(form=form)





# def update_tv_show_view(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     if request.method == 'POST':
#         form = forms.TvShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2> Фильм успешно обновлен!</h2>')
#     else:
#         form = forms.TvShowForm(instance=show_object)
#
#     return render(request, 'update_tv_show.html', {
#                                                     'form': form,
#                                                     'object': show_object
#                                                    })


class TvShowDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=show_id)


# def delete_tv_show_view(request, id):
#     show_object = get_object_or_404(models.TVShow, id=id)
#     show_object.delete()
#     return HttpResponse('<h2>Фильм успешно удален</h2>')