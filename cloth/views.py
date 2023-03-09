from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ClothListOneView(ListView):
    queryset = models.Cloth.objects.filter(tags__name="Мужская одежда")

    template_name = "cloth_list_one.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name="Мужская одежда")


class ClothListTwoView(ListView):
    queryset = models.Cloth.objects.filter(tags__name="Женская одежда")

    template_name = "cloth_list_two.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name="Женская одежда")


class ClothListThreeView(ListView):
    queryset = models.Cloth.objects.filter(tags__name="Одежда для подростков")

    template_name = "cloth_list_three.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name="Одежда для подростков")


class ClothListFourView(ListView):
    queryset = models.Cloth.objects.filter(tags__name="Одежда для детей")

    template_name = "cloth_list_four.html"

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name="Одежда для детей")


class ClothDetailView(DetailView):
    template_name = "cloth_detail.html"

    def get_object(self, **kwargs):
        cloth_id = self.kwargs.get("id")
        return get_object_or_404(models.Cloth, id=cloth_id)


class OrderCreateView(CreateView):
    template_name = "add-order.html"
    form_class = forms.OrderForm
    success_url = "/cloths/"
    queryset = models.Order.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
