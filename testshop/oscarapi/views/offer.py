from rest_framework import generics
from rest_framework.response import Response


from oscar.core.loading import get_class, get_model

from oscarapi.utils.categories import find_from_full_slug
from oscarapi.utils.loading import get_api_classes, get_api_class


(
    BenefitSerializer,
    ConditionOfferSerializer,
    ConditionSerializer,
) = get_api_classes(
    "serializers.offer",
    [
        "BenefitSerializer",
        "ConditionOfferSerializer",
        "ConditionSerializer",
    ],
)

Benefit = get_model("offer", "Benefit")
ConditionalOffer = get_model("offer", "ConditionalOffer")
Condition = get_model("offer", "Condition")
Range = get_model("offer", "Range")

class BenefitList(generics.ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


class BenefitDetail(generics.RetrieveAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class ConditionalOfferList(generics.ListAPIView):
    queryset = ConditionalOffer.objects.all()
    serializer_class = ConditionOfferSerializer

class ConditionalOfferDetail(generics.RetrieveAPIView):
    queryset = ConditionalOffer.objects.all()
    serializer_class = ConditionOfferSerializer

class ConditionList(generics.ListAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer

class ConditionDetail(generics.RetrieveAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer



