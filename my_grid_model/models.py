from django.db import models

# Create your models here.

class BaseCell(models.Model):
    column = models.IntegerField()
    column_label = models.CharField(max_length=3)
    row = models.IntegerField()
    row_label = models.CharField(max_length=3)
    value = models.CharField(max_length=64)

    class Meta:
        abstract = True

class BaseRow(models.Model):

    class Meta:
        abstract = True

class BaseColumn(models.Model):

    class Meta:
        abstract = True

class BaseGrid(models.model):

    class Meta:
        abstract = True
