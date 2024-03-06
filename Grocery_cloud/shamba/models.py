from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.product_name


class orderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.ordered}"


class customer(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    profile_pic = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.first_name

    def edit(self, first_name, last_name, email, profile_pic):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.profile_pic = profile_pic
        self.save(first_name.lower(), last_name.lower(), email.lower(), profile_pic)


class Item(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    ordered = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.quantity} of {self}"


class Payment(models.Model):
    phone_number = models.CharField(max_length=10, unique=True)
    reference_number = models.CharField(max_length=10, unique=True)
    amount = models.DecimalField(max_digits=40000, decimal_places=2)

    def __str__(self):
        return f"{self}"
