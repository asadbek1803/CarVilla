from django.db import models


class New_cars(models.Model):
    car_image = models.ImageField(null=True, blank=True, default='static/home/images/new-cars-model/ncm1.png', upload_to='images/new-cars/')
    car_name = models.CharField(max_length=140, default="BMX | M5")
    car_about = models.TextField(default="This is car about")


    def __str__(self):
        return self.car_name

    class Meta:
        db_table = "New_car"
