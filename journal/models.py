from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.

''' 
    trade journal table
'''
class PositionSide(models.TextChoices):
    LONG = 'LONG', 'Long'
    SHORT = 'SHORT', 'Short'

class PositionType(models.TextChoices):
    MARKET = 'MARKET', 'Market'
    LIMIT = 'LIMIT', 'Limit'
    STOP = 'STOP', 'Stop' 
class Trade (models.Model):
    open_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    close_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    active_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    open_price = models.DecimalField(max_digits=20, decimal_places=10, validators=[MinValueValidator(0.0)])
    close_price = models.DecimalField(max_digits=20, decimal_places=10, validators=[MinValueValidator(0.0)])
    position_side = models.CharField(max_length=10, choices=PositionSide.choices)
    position_type = models.CharField(max_length=10 , choices=PositionType.choices)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Trade {self.id}: {self.position_side} Open: {self.open_time} Close: {self.close_time}"

