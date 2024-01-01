from django.utils import timezone
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=10, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.00)
    quality_rating_avg = models.FloatField(default=0.00)
    average_response_time = models.FloatField(default=0.00)
    fulfillment_rate = models.FloatField(default=0.00)

    def __str__(self):
        return self.name
    
    def generate_vendor_code(self):
        self.vendor_code=f"Vendor {str(self.id).zfill(3)}"
        self.save(update_fields=["vendor_code"])
        return self.vendor_code
        
    
class PurchaseOrder(models.Model):
    class PurchaseOrderStatus(models.TextChoices):
        PENDING = "pending","Pending"
        COMPLETED = "completed","Completed"
        CANCELED = "canceled","Canceled"
        
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)  
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.vendor.name} - PO {self.po_number}"


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,related_name="vendor_history")
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-date']