from django_filters import FilterSet
from .models import Post


class ProductFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            '_post_rating': ['gt'],
            'date_creation': ['date__gte'],
            'author__user__username': ['icontains'],
            'category__category': ['icontains'],
        }
