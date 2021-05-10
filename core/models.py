from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    class Meta:
        abstract = True

class Order(CommonInfo):

    JSW = 'JSW'
    Dalmia = 'Dalmia'
    Ultratech = 'Ultratech'

    CEMENT_CHOICES = [
        (JSW, 'JSW'),
        (Dalmia, 'Dalmia'),
        (Ultratech, 'Ultratech'),
        ]

    phone = models.CharField(max_length=10)
    total = models.CharField(max_length=4)
    brand = models.CharField(max_length=30, choices=CEMENT_CHOICES, default=JSW,)

    def __unicode__(self):
        return self.name

class Contact(CommonInfo):

    message = models.TextField()

    def __unicode__(self):
        return self.name
