from django_filters.rest_framework import FilterSet, filters
from api.models import *


class ProduceFilter(FilterSet):
    order = filters.CharFilter(method='produce_order_filter')
    o_phone_num = filters.CharFilter(method='produce_order_filter')

    def produce_order_filter(self, queryset, order, o_phone_num, value1, value2):
        order = self.request.query_params.get(order, value1)
        if order is not None:
            if o_phone_num is not None:
                queryset = queryset.filter(order__icontains=value1, o_phone_num__icontains=value2)
        return queryset
