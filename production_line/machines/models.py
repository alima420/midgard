from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    counter = models.IntegerField()

    def __str__(self):
        return self.name
    

class LogisticsBox(models.Model):
    logistics_box_id = models.AutoField(primary_key=True)  # Automatically increments and serves as the primary key
    details = models.CharField(max_length=255)  # Description or details of the box
    flag = models.BooleanField(default=False)

    def __str__(self):
        return f"Box ID {self.logistics_box_id}: {self.details}"

class Exception(models.Model):
    logistics_box = models.ForeignKey(LogisticsBox, on_delete=models.CASCADE, related_name='exceptions')
    serial_number = models.CharField(max_length=255)  # Serial number of the item
    details = models.CharField(max_length=255)  # Description of the exception
    flag = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Exception {self.serial_number} for Box ID {self.logistics_box_id}"
    
class ProductBox(models.Model):
    logistics_box_id = models.IntegerField()
    logistics_box_timestamp = models.DateTimeField()
    number_units = models.IntegerField()
    article_number = models.CharField(max_length=255)
    product_box_id = models.IntegerField()
    product_serial = models.CharField(max_length=255, db_index=True)
    device_creation_timestamp = models.DateTimeField()
    device_remarks = models.CharField(max_length=255)

    def __str__(self):
        return f"ProductBox ID {self.product_box_id} with Serial {self.product_serial}"