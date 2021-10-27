
from django.utils.translation import ugettext as _
from rest_framework import serializers
from oscar.core.loading import get_model

from oscarapi.utils.settings import overridable
from oscarapi.serializers.utils import (
    OscarHyperlinkedModelSerializer,
)


Benefit = get_model("offer", "Benefit")
ConditionalOffer = get_model("offer", "ConditionalOffer")
Condition = get_model("offer", "Condition")

class BenefitSerializer(OscarHyperlinkedModelSerializer):

    class Meta:
        model = Benefit
        fields = '__all__'


class ConditionOfferSerializer(OscarHyperlinkedModelSerializer):

    class Meta:
        model = ConditionalOffer
        fields = '__all__'


class ConditionSerializer(OscarHyperlinkedModelSerializer):

    class Meta:
        model = Condition
        fields = '__all__'

