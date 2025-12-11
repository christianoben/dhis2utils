from django.db import models
from django.utils import timezone


class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='sub_counties')
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('county', 'name')

    def __str__(self):
        return f"{self.name} ({self.county})"


class Ward(models.Model):
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE, related_name='wards')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('sub_county', 'name')

    def __str__(self):
        return f"{self.name} ({self.sub_county})"
