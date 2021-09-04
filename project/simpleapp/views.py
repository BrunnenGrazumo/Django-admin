from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Category
from django.core.paginator import Paginator
from .search import ProductFilter
from .forms import ProductForm
from django.core.mail import send_mail
from .models import Appointment



class ProductsList(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    ordering = ['-id']
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required =('simpleapp.change_post')
    template_name = 'post_update.html'
    form_class = ProductForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class ProductDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post')
    template_name = 'post_create.html'
    form_class = ProductForm


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post')
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/post/'


class ProductSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'post'
    ordering = ['-id']
    paginate_by = 10
    form_class = ProductForm

    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'filter': self.get_filter(),
            'categories': Category.objects.all(),
            'form': ProductForm()
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

class CatSearch(ListView):
    model = Post
    template_name = 'categories.html'
    context_object_name = 'post'
    ordering = ['-id']
    paginate_by = 10
    form_class = ProductForm

    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'filter': self.get_filter(),
            'categories': Category.objects.all(),
            'form': ProductForm()
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)





class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            # имя клиента и дата записи будут в теме для удобства
            message=appointment.message,  # сообщение с кратким описанием проблемы
            from_email='razumov.maxim2016@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
            recipient_list=[]  # здесь список получателей. Например, секретарь, сам врач и т. д.
        )

        return redirect('appointments:make_appointment')