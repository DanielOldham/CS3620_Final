from django.db import models


# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(default='component_images/default_component.png', upload_to='component_images')
    link = models.URLField()

    def __str__(self):
        return self.name

    def get_type(self):
        try:
            if self.cpu is not None:
                return 'CPU'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.ram is not None:
                return 'RAM'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.graphics is not None:
                return 'Graphics'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.case is not None:
                return 'Case'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.motherboard is not None:
                return 'Motherboard'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.storage is not None:
                return 'Storage'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.powersupply is not None:
                return 'PowerSupply'
        except models.ObjectDoesNotExist:
            pass

        try:
            if self.cooler is not None:
                return 'Cooler'
        except models.ObjectDoesNotExist:
            pass

        return None

    def get_child(self):
        try:
            return self.cpu
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.ram
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.graphics
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.case
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.motherboard
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.storage
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.powersupply
        except models.ObjectDoesNotExist:
            pass

        try:
            return self.cooler
        except models.ObjectDoesNotExist:
            pass

        return None


class CPU(Component):
    # speed is in GHz
    speed = models.FloatField()


class RAM(Component):
    # speed is in MHz
    speed = models.FloatField()
    # size is in GBytes
    size = models.FloatField()


class Graphics(Component):
    # amount of vram in GBytes
    size = models.FloatField()


class Case(Component):
    color = models.CharField(max_length=50)


class Motherboard(Component):
    socket = models.CharField(max_length=50)


class Storage(Component):
    # size is in GBytes
    size = models.FloatField()


class PowerSupply(Component):
    # power is in Watts
    power = models.IntegerField()


class Cooler(Component):
    type = models.CharField(max_length=50)
