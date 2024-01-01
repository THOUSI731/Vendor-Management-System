from django.shortcuts import render
from rest_framework.views import APIView
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .api.serializers import VendorModelSerializer,VendorPOSTSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class VendorListCreateAPIView(APIView):
    def get(self,request):
        instance=Vendor.objects.all()
        serializer=VendorModelSerializer(instance,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=VendorPOSTSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        vendor=Vendor.objects.create(
            name=serializer.validated_data.get("name",None),
            contact_details=serializer.validated_data.get("contact_details",None),
            address=serializer.validated_data.get("address",None)
        )
        vendor.generate_vendor_code()
        return Response(VendorModelSerializer(vendor).data,status=status.HTTP_201_CREATED)

class VendorDetailUpdateAPIView(APIView):
    def get_queryset(self,pk):
        try:
            return Vendor.objects.get(id=pk)
        except Vendor.DoesNotExist:
            raise Response({"msg":"Vendor Does not Exist"},status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,pk):
        instance=self.get_queryset(pk)
        serializer=VendorModelSerializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        instance=self.get_queryset(pk)
        serializer=VendorModelSerializer(instance)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        instance.name=serializer.validated_data.get("name",instance.name)
        instance.contact_details=serializer.validated_data.get("contact_details",instance.contact_details)
        instance.address=serializer.validated_data.get("address",instance.address)
        instance.on_time_delivery_rate=serializer.validated_data.get("on_time_delivery_rate",instance.on_time_delivery_rate)
        instance.quality_rating_avg=serializer.validated_data.get("quality_rating_avg",instance.quality_rating_avg)
        instance.average_response_time=serializer.validated_data.get("average_response_time",instance.average_response_time)
        instance.fulfillment_rate=serializer.validated_data.get("fulfillment_rate",instance.fulfillment_rate)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        instance=self.get_queryset(pk)
        instance.delete()
        return Response({"msg":"Vendor Deleted Successfully"},status=status.HTTP_200_OK)
    

        
    
    