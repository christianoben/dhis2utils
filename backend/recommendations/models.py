from django.db import models
from django.utils import timezone


class RecommendedMatch(models.Model):
    OPEN = 'OPEN'
    USED = 'USED'
    DISMISSED = 'DISMISSED'
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (USED, 'Used'),
        (DISMISSED, 'Dismissed'),
    ]

    pool = models.ForeignKey('pools.Pool', on_delete=models.CASCADE, related_name='recommended_matches')
    player1 = models.ForeignKey('accounts.Player', on_delete=models.CASCADE, related_name='recommended_as_player1')
    player2 = models.ForeignKey('accounts.Player', on_delete=models.CASCADE, related_name='recommended_as_player2')
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=OPEN)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['pool']),
            models.Index(fields=['player1', 'player2']),
        ]

    def __str__(self):
        return f"Recommendation at {self.pool}: {self.player1} vs {self.player2}"
