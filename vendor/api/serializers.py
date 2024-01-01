from ..models import Vendor,PurchaseOrder,HistoricalPerformance
from rest_framework import serializers

class VendorPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=("name","contact_details","address")

class VendorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=("name","contact_details","address","vendor_code","on_time_delivery_rate","quality_rating_avg","average_response_time","fulfillment_rate")

class PurchaseOrderPOSTSerializier(serializers.ModelSerializer):
    vendor=serializers.PrimaryKeyRelatedField()
    class Meta:
        model=PurchaseOrder
        fields=("vendor","po_number","order_date","delivery_date","items","quantity","status","quality_rating","issue_date","acknowledgment_date")