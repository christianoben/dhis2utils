from django.db import models
from django.utils import timezone


class Game(models.Model):
    PENDING_APPROVAL = 'PENDING_APPROVAL'
    ACCEPTED = 'ACCEPTED'
    IN_PLAY = 'IN_PLAY'
    RESULT_PENDING = 'RESULT_PENDING'
    FINISHED = 'FINISHED'
    REJECTED = 'REJECTED'
    DISPUTED = 'DISPUTED'
    EXPIRED = 'EXPIRED'
    STATUS_CHOICES = [
        (PENDING_APPROVAL, 'Pending approval'),
        (ACCEPTED, 'Accepted'),
        (IN_PLAY, 'In play'),
        (RESULT_PENDING, 'Result pending'),
        (FINISHED, 'Finished'),
        (REJECTED, 'Rejected'),
        (DISPUTED, 'Disputed'),
        (EXPIRED, 'Expired'),
    ]

    pool = models.ForeignKey('pools.Pool', on_delete=models.CASCADE, related_name='games')
    player1 = models.ForeignKey('accounts.Player', on_delete=models.CASCADE, related_name='games_as_player1')
    player2 = models.ForeignKey('accounts.Player', on_delete=models.CASCADE, related_name='games_as_player2')
    initiated_by = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='initiated_games')
    accepted_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='accepted_games')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=PENDING_APPROVAL)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey('accounts.Player', on_delete=models.SET_NULL, null=True, blank=True, related_name='wins')
    score_player1 = models.IntegerField(null=True, blank=True)
    score_player2 = models.IntegerField(null=True, blank=True)
    result_submitted_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='submitted_results')
    result_confirmed_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='confirmed_results')
    dispute_flag = models.BooleanField(default=False)
    dispute_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['pool']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"Game {self.id} at {self.pool}"
