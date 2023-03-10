from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinValueValidator

# Create your models here.
STATE_CHOICE =(
    ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','chandigarh'),
    ('chhattisgarh','chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('haryana','haryana'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('manipur','manipur'),
    ('meghlaya','meghalaya'),
    ('Uttar pradesh','Uttar pradesh'),
    ('noida','noida'),
)

class Customer(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    locality =models.CharField(max_length=200)
    city = models.CharField(max_length=40)
    Zipcode =models.IntegerField()
    state =models.CharField(choices= STATE_CHOICE, max_length=50)


    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES =(
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('Tw', 'Topwear'),
    ('Bw', 'Bootomwear'),

)

class Product(models.Model):
    title =models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price= models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices= CATEGORY_CHOICES, max_length=2)
    product_image =models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def toral_cost(self):
        return self.quantity *str.product.discounted_price
STATE_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date =models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATE_CHOICE,default='Pending')

    @property
    def toral_cost(self):
        return self.quantity * str.product.discounted_price

