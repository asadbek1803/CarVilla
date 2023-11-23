from django.db import models

class Clients(models.Model):
    client_image = models.ImageField(blank=True, null=True, default="static/home/images/clients/c1.png", upload_to='images/clients/')
    message = models.TextField(default="This is client message")
    client_full_name = models.CharField(max_length=140)
    country = models.CharField(max_length=140)

    def __str__(self):
        return f"Client: {self.client_full_name}"

