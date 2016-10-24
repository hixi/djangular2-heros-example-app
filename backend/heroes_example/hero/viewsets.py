from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import Hero
from .serializers import HeroSerializer


class HeroFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Hero
        fields = ['name']


class HeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name',)
    filter_class = HeroFilter
