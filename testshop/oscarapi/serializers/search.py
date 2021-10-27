from django.utils.translation import ugettext as _
from rest_framework import serializers
from oscar.core.loading import get_model

from oscarapi.utils.settings import overridable
from oscarapi.serializers.utils import (
    OscarHyperlinkedModelSerializer,
)
from haystack.query import SearchQuerySet

Product = get_model("catalogue", "Product")


class SearchSerializer(serializers.Serializer):

    id = serializers.CharField()
    django_ct = serializers.CharField()
    django_id = serializers.CharField()
    text = serializers.CharField()
    upc = serializers.CharField()
    title = serializers.CharField()
    title_exact = serializers.CharField()
    product_class = serializers.CharField()
    product_class_exact = serializers.CharField()
    category = serializers.CharField()
    category_exact = serializers.CharField()
    suggestions = serializers.CharField()
    date_created = serializers.CharField()
    date_updated = serializers.CharField()
    title_s = serializers.CharField()
    _version_ = serializers.IntegerField()


    
    

     