# Uncomment the following imports before adding the Model code

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# from django.utils.timezone import now

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:


class CarMake(models.Model):
    """
    - Name
    - Description
    - Any other fields you would like to include in car make model
    - __str__ method to print a car make object
    """

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    """
    - Many-To-One relationship to Car Make model (One Car Make has many
    Car Models, using ForeignKey field)
    - Name
    - Type (CharField with a choices argument to provide limited choices
    such as Sedan, SUV, WAGON, etc.)
    - Year (IntegerField) with min value 2015 and max value 2023
    - Any other fields you would like to include in car model
    - __str__ method to print a car make object
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    TYPE_CHOICES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
    ]
    type = models.CharField(
        max_length=5,
        choices=TYPE_CHOICES,
        default=SEDAN,
    )
    year = models.IntegerField(
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    def __str__(self):
        return str(self.name)
