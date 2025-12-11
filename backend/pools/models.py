from django.db import models
from django.utils import timezone


class Pool(models.Model):
    PENDING_APPROVAL = 'PENDING_APPROVAL'
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    STATUS_CHOICES = [
        (PENDING_APPROVAL, 'Pending approval'),
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    price_per_game = models.DecimalField(max_digits=10, decimal_places=2)
    ward = models.ForeignKey('locations.Ward', on_delete=models.PROTECT, related_name='pools')
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='pools')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=PENDING_APPROVAL)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['ward']),
            models.Index(fields=['owner']),
        ]

    def __str__(self):
        return self.name
