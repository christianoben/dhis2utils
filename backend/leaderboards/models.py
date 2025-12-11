from django.db import models
from django.utils import timezone


class LeaderboardEntry(models.Model):
    POOL = 'POOL'
    WARD = 'WARD'
    SUB_COUNTY = 'SUB_COUNTY'
    COUNTY = 'COUNTY'
    NATIONAL = 'NATIONAL'
    SCOPE_CHOICES = [
        (POOL, 'Pool'),
        (WARD, 'Ward'),
        (SUB_COUNTY, 'Sub-county'),
        (COUNTY, 'County'),
        (NATIONAL, 'National'),
    ]

    ALL_TIME = 'ALL_TIME'
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    PERIOD_CHOICES = [
        (ALL_TIME, 'All time'),
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
    ]

    scope_type = models.CharField(max_length=20, choices=SCOPE_CHOICES)
    scope_id = models.BigIntegerField(null=True, blank=True)
    player = models.ForeignKey('accounts.Player', on_delete=models.CASCADE)
    period_type = models.CharField(max_length=20, choices=PERIOD_CHOICES)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['scope_type', 'scope_id', 'period_type', 'period_start', 'period_end']),
            models.Index(fields=['player']),
        ]

    def __str__(self):
        return f"{self.player} - {self.scope_type} {self.period_type}"
