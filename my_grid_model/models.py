from django.db import models

class SimpleGrid(models.Model):
    name = models.CharField(
        max_length=128
    )
    data = models.JSONField(
        default=dict, 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.name
