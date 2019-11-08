import datetime as dt

from django.core.exceptions import ValidationError
from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=200, null=True)

    rows = models.IntegerField()
    elevations = models.IntegerField()  # y
    positions = models.IntegerField()  # x

    default_height = models.DecimalField(decimal_places=2, max_digits=9, default=1)
    default_length = models.DecimalField(decimal_places=2, max_digits=9, default=1)
    default_width = models.DecimalField(decimal_places=2, max_digits=9, default=1)

    def __str__(self):
        return str(self.name) + ', rs: ' + str(self.rows) + ' es: ' + str(self.elevations) + ' ps: ' + str(
            self.positions)


class Cell(models.Model):
    row = models.IntegerField()
    elevation = models.IntegerField()  # y
    position = models.IntegerField()  # x

    height = models.DecimalField(decimal_places=2, max_digits=9, default=1)
    length = models.DecimalField(decimal_places=2, max_digits=9, default=1)
    width = models.DecimalField(decimal_places=2, max_digits=9, default=1)

    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('row', 'elevation', 'position', 'storage'),)

    def __str__(self):
        return 'r: ' + str(self.row) + ' e: ' + str(self.elevation) + ' p: ' + str(self.position)

    def clean(self):
        if self.storage.rows * self.storage.elevations * self.storage.positions >= len(
                Cell.objects.filter(storage=self.storage)):
            raise ValidationError('You cannot create more cells for this storage')


class Cargo(models.Model):
    # cargo_ID = models.IntegerField(unique=True, primary_key=True)

    # row = models.IntegerField()
    # elevation = models.IntegerField()
    # position = models.IntegerField()
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE)

    height = models.DecimalField(decimal_places=2, max_digits=9, default=1)
    length = models.DecimalField(decimal_places=2, max_digits=9, default=1)
    width = models.DecimalField(decimal_places=2, max_digits=9, default=1)

    description = models.CharField(max_length=500)
    title = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now=True)
    date_dated = models.DateField(default=dt.datetime.now)

    rotatable = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + ": " + str(self.title)
