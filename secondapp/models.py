from django.db import models
from django.contrib.auth.models import User
import datetime


class Contact_Us(models.Model):
    name = models.CharField(max_length=250)
    contact_number = models.IntegerField(blank=True, unique=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"


class Category(models.Model):
    cat_name = models.CharField(max_length=250)
    cover_pic = models.FileField(upload_to="media/%Y/%m/%d")
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name


class register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.BigIntegerField()
    profile_pic = models.ImageField(
        upload_to="profiles/%Y/%m/%d", null=True, blank=True)
    age = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=250, default="Male")
    address = models.CharField(max_length=250, null=True, blank=True)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username


class add_product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.FloatField()
    sale_price = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to="products/%Y/%m/%d")
    details = models.TextField()
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name


class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    product = models.ForeignKey(add_product, on_delete=models.CASCADE,null=True)
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_id.username


class balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    wallet_balance = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
class Review(models.Model):
    name = models.CharField(max_length=30 , null = True)
    contact = models.BigIntegerField(default=1,null=True)
    product_id = models.ForeignKey(add_product, on_delete=models.CASCADE)
    review = models.CharField(max_length=250)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_id.product_name





