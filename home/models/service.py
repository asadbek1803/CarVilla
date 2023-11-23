from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=110, verbose_name="title", default="This is title")
    about = models.TextField(verbose_name="About", default="This is about")


    def __str__(self):
        return self.title

    class Meta:
        db_table = "Servis"
