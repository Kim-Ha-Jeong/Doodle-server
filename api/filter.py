from django_filters.rest_framework import FilterSet, filters
from api.models import *


class ProduceFilter(FilterSet):
    order = filters.CharFilter(method='produce_filter')
    #o_phone_num = filters.CharFilter(method='produce_filter')

    def produce_filter(self, queryset, value):
        order = str(self.request.POST['order'])
        #o_phone_num = str(self.request.POST['o_phone_num'])
        if order is not None: #and o_phone_num is not None:
            queryset = queryset.filter(order__icontains=value)
        print("성공")

    class Meta:
        model = Produce
        fields = ['order', 'o_phone_num']
