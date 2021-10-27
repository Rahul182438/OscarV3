
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from oscar.apps.customer.signals import user_registered
from oscar.core.loading import get_class, get_model

from oscarapi.utils.session import login_and_upgrade_session
from oscarapi.utils.loading import get_api_classes
from oscarapi.basket import operations
from oscarapi.pagination import CustomPagination
from haystack.query import SearchQuerySet

(
    SearchSerializer,
) = get_api_classes(
    "serializers.search",
    [
        "SearchSerializer",
    ],
)


Product = get_model("catalogue", "Product")

class SearchView(APIView):

    queryset = Product.objects.all()
    pagination_class = CustomPagination
    
    def get(self,request,format=None,**kwargs):
        
        search_filter = self.request.GET.get('q')
        prods = SearchQuerySet().filter(title=search_filter).facet('product_class')
        facet = prods.facet_counts()
        serializer = SearchSerializer(prods,many=True)     

        return Response({'Response':serializer.data, 'Facet Response':facet})
    