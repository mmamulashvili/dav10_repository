from django.db import models
\

class ModelOne(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def display_name(self):
        return self.name

    def __str__(self):
        return self.name


class ModelTwo(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def display_price(self):
        return str(self.price)

    def __str__(self):
        return self.description[:20]


class ModelThree(models.Model):
    email = models.EmailField()
    rating = models.FloatField()
    joined_on = models.DateField()

    def display_email(self):
        return self.email

    def __str__(self):
        return self.email
