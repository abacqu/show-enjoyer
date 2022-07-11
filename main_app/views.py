from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Show, Category, Photo
import uuid
import boto3
from django.contrib.auth.forms import UserCreationForm

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'showenjoyer'

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def shows_index(request):
  shows = Show.objects.filter(user=request.user)
  return render(request, 'shows/index.html', { 'shows': shows })

@login_required
def shows_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  categories_show_doesnt_have = Category.objects.exclude(id__in = show.categories.all().values_list('id'))
  return render(request, 'shows/detail.html', {
    'show': show, 
    'categories': categories_show_doesnt_have
  })

@login_required
def assoc_category(request, show_id, category_id):
  Show.objects.get(id=show_id).categories.add(category_id)
  return redirect('detail', show_id=show_id)

@login_required
def assoc_category_delete(request, show_id, category_id):
  Show.objects.get(id=show_id).categories.remove(category_id)
  return redirect('detail', show_id=show_id)

@login_required
def add_photo(request, show_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            print(url)
            photo = Photo(url=url, show_id=show_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', show_id=show_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class ShowCreate(LoginRequiredMixin, CreateView):
  model = Show
  fields = ['name', 'date', 'songs', 'reflection']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)
  

class ShowUpdate(LoginRequiredMixin, UpdateView):
  model = Show
  fields = ['name', 'date', 'songs', 'reflection']

class ShowDelete(LoginRequiredMixin, DeleteView):
  model = Show
  success_url = '/shows/'


class CategoryList(LoginRequiredMixin, ListView):
  model = Category
  template_name = 'categories/index.html'

class CategoryDetail(LoginRequiredMixin, DetailView):
  model = Category
  template_name = 'categories/detail.html'

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = '/categories/'
