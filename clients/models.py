# clients/models.py
from django.db import models

class Client(models.Model):
    PRODUCT_CHOICES = [
        ('A', 'Product A'),
        ('B', 'Product B'),
        ('C', 'Product C'),
        ('D', 'Product D'),
        ('E', 'Product E'),
        ('F', 'Product F'),
    ]

    company_name = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    system_user = models.BooleanField(default=False)
    offered_product = models.CharField(max_length=1, choices=PRODUCT_CHOICES, blank=True, null=True)
    potential_market_share = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    potential_yearly_sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    last_action = models.TextField(blank=True, null=True)
    next_action = models.TextField(blank=True, null=True)
    comment_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name