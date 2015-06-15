from django.db import models
from django.shortcuts import get_object_or_404


class MenuItem(models.Model):
    class Meta:
        ordering = ['order']

    group = models.ForeignKey('MenuGroup', related_name='items')
    order = models.IntegerField()
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class MenuGroup(models.Model):
    class Meta:
        ordering = ['order']
    heading = models.CharField(max_length=32, blank=True)
    menu = models.ForeignKey('Menu', related_name='groups')
    name = models.CharField(max_length=24)
    order = models.IntegerField()

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=24, unique=True)

    def __unicode__(self):
        return self.name

    def groupNamed(self, name):
        return get_object_or_404(MenuGroup, name=name)