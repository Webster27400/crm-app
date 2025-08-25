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

    STATUS_CHOICES = [
        ('Progressing', 'Progressing'),
        ('On Hold', 'On Hold'),
        ('Win', 'Win'),
        ('Lost', 'Lost'),
    ]

    MARKET_SHARE_CHOICES = [
        (25, '25%'),
        (50, '50%'),
        (75, '75%'),
        (100, '100%'),
    ]
    
    ROADBLOCK_CHOICES = [ # Nowa lista opcji
        ('Budget freeze', 'Budget freeze'),
        ('Stakeholder unvailable', 'Stakeholder unvailable'),
        ('Needs approval', 'Needs approval'),
        ('Technical issue', 'Technical issue'),
        ('Resource limitation', 'Resource limitation'),
        ('Pricing negotiation', 'Pricing negotiation'),
        ('Project postponed', 'Project postponed'),
    ]
    
    company_name = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    system_user = models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Progressing')
    reason_for_roadblock = models.CharField(max_length=50, choices=ROADBLOCK_CHOICES, blank=True, null=True)
    offered_product = models.CharField(max_length=1, choices=PRODUCT_CHOICES, blank=True, null=True)
    potential_market_share = models.IntegerField(choices=MARKET_SHARE_CHOICES, blank=True, null=True)
    potential_yearly_sales = models.IntegerField(blank=True, null=True)
    last_action = models.TextField(blank=True, null=True)
    next_action = models.TextField(blank=True, null=True)
    comment_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name