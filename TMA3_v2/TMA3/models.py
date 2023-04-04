from django.db import models

# Part 2 Images class
class Image(models.Model):
    image_name = models.CharField(max_length=140, blank=False, null=False)
    image_location = models.CharField(max_length=140, blank=False, null=False)
    image_caption = models.CharField(max_length=140, blank=False, null=False)
    
    def __str__(self):
        return self.image_location
    
class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_firstname = models.CharField(max_length=140, blank=False, null=False)
    customer_lastname = models.CharField(max_length=140, blank=False, null=False)
    customer_email = models.CharField(max_length=140, blank=False, null=False)
    customer_pass = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.customer_firstname
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=140, blank=False, null=False)
    product_image = models.CharField(max_length=140, blank=False, null=False)
    product_price = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.BigAutoField(primary_key=True)

    def __int__(self):
        return self.order_id
    
class Cart(models.Model):
    cart_product_name = models.CharField(max_length=140, blank=False, null=False)
    cart_product_image = models.CharField(max_length=140, blank=False, null=False)
    cart_product_price = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.cart_product_name


    

    


    
    
    
