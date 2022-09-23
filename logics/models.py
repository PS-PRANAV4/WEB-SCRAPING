from pyexpat import model
from django.db import models
from rest_framework import serializers

# Create your models here.
class Plan(models.Model):
    price = models.TextField()
    details = models.TextField()

    def __ste__(self):
        return self.price



class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('price', 'details')
