from django.db import models
from django.utils import timezone

class Dish(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def change_price(self, price):
        self.price = price
        self.save()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    Cities=(
        ('M','Москва'),
        ('S-P','Санкт-Петербург'),
    )
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=4, choices=Cities)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUSES =(
    ('D', 'Заказ отменён'),
    ('A', 'Заказ принят'),
    ('F','Заказ завершён'),
    )
    rest_name = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    made_on = models.DateTimeField()
    consists_of = models.ManyToManyField(Dish)
    num_of_dishes = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUSES)

    def change_state(self, new_state):
        self.status = new_state
        self.save()

    def __str__(self):
        return str(self.id)
