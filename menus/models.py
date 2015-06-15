from django.db import models

class MenuItem(models.Model):
    live = models.BooleanField(default=False)
    order = models.IntegerField()
    show_in_menu = models.BooleanField(default=False)
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
