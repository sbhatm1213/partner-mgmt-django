from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Distributor, Partner
from .serializers import DistributorSerializer, PartnerSerializer
from .hubspot import sync_partner_to_hubspot


@api_view(["POST", "GET"])
def distributors(request):
    if request.method == "POST":
        serializer = DistributorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    data = DistributorSerializer(Distributor.objects.all(), many=True).data
    return Response(data)


@api_view(["POST", "GET"])
def partners(request, distributor_id):
    if request.method == "POST":
        serializer = PartnerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(distributor_id=distributor_id)
        return Response(serializer.data, status=201)

    data = PartnerSerializer(Partner.objects.filter(distributor__id=distributor_id), many=True).data
    return Response(data)


@api_view(["POST"])
def sync_partner(request, partner_id):
    partner = Partner.objects.get(id=partner_id)
    hubspot_id = sync_partner_to_hubspot(partner)
    partner.hubspot_company_id = hubspot_id
    partner.save()
    return Response({"hubspot_company_id": hubspot_id})
