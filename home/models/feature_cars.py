from django.db import models

class Feature_cars(models.Model):
    type_cars = (
        ('mexanik', 'Mexanik'),
        ('automatic', 'Automatic')
    )
    image = models.ImageField(blank=True, null=True, default='static/home/images/new-cars-model/ncm1.png', upload_to='images/featured-cars/')
    year = models.PositiveSmallIntegerField(default=2017)
    model = models.CharField(max_length=45, default="3100 Mi")
    horse_power = models.PositiveSmallIntegerField(default=240)
    car_type = models.CharField(max_length=14, choices=type_cars)
    car_name = models.CharField(max_length=140, default='BMW 6-Series Gran Coupe')
    price = models.CharField(max_length=20, default="$500,500")
    about = models.TextField(default="This is car about for sale")


    def __str__(self):
        return f"{self.car_name} sell {self.price}"



