from django.forms import ModelForm
from .models import Post



class ProductForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category']