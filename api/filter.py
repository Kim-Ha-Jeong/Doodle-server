from django_filters.rest_framework import FilterSet, filters
from api.models import *


class ProduceFilter(FilterSet):
    order = filters.CharFilter(method='produce_order_filter')
    o_phone_num = filters.CharFilter(method='produce_order_filter')

    def produce_order_filter(self, queryset, order, value):
        order = self.request.query_params.get(order, value)
        if order is not None:
            queryset = queryset.filter(order__icontains=value)
        return queryset

    def produce_phone_filter(self, queryset, o_phone_num, value):
        o_phone_num = self.request.query_params.get(o_phone_num, value)
        if o_phone_num is not None:
            queryset = queryset.filter(o_phone_num__icontains=value)
        return queryset
