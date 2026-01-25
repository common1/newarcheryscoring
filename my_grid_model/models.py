from django.db import models

# Create your models here.

class BaseCell(models.Model):
    value = models.CharField(max_length=64)

    previous_column = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    next_column = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    previous_row = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    next_row = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True

class BaseGrid(models.Model):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def create(cls, x, y):
        return cls(x = x, y = y)

