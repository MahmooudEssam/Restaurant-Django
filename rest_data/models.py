from django.db import models
from . constants import genderchoice
# Create your models here.
class Customer_acc(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    tel=models.PositiveIntegerField()
    DOB=models.DateField()

class Resv_rec(models.Model):
    seatsNum=models.IntegerField()
    cu_no=models.ForeignKey(Customer_acc,on_delete=models.CASCADE)



class Rest_tab(models.Model):
    tableNum=models.OneToOneField(Resv_rec,on_delete=models.CASCADE)
    status=models.TextField()
    

class Rest_seats(models.Model):
    tableNum=models.ForeignKey(Rest_tab,on_delete=models.CASCADE)
    status=models.TextField()
    seatsNum=models.OneToOneField(Resv_rec,on_delete=models.CASCADE)



class Employee(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField( max_length=20 ,choices=genderchoice)
    DOB=models.DateField()
    email=models.EmailField(max_length=200)
    tel=models.PositiveIntegerField()
    salary=models.FloatField()


class Menu_rec(models.Model):
    name=models.CharField(max_length=20)
    img=models.URLField()
    desc=models.TextField()
    ingredients=models.TextField()
    promos=models.TextField()
    price=models.FloatField()


class Order_rec(models.Model):
    menu_ID=models.ForeignKey(Menu_rec,on_delete=models.CASCADE)
    table_Num=models.PositiveBigIntegerField()
    order_time=models.DateTimeField()
    E_ID=models.ForeignKey(Employee,on_delete=models.CASCADE)
