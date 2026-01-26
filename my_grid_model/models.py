from django.db import models

class BaseCell(models.Model):
    value = models.CharField(max_length=64)

    previous_column = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    next_column = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    previous_row = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    next_row = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True

class SimpleGrid(models.Model):
    name = models.CharField(max_length=128)
    data = models.JSONField(null=True)
        
    def __str__(self):
        return self.name
    