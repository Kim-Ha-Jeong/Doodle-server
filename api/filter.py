from django_filters.rest_framework import FilterSet, filters
from api.models import *


class ProduceFilter(FilterSet):
    order = filters.CharFilter(method='produce_order_filter')
    #o_phone_num = filters.CharFilter(method='produce_phone_filter')

    def produce_order_filter(self, queryset, order, value):
        order = self.request.query_params.get(order, value)
        if order is not None:
            queryset = queryset.filter(order__icontains=value)
        return queryset
