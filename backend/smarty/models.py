from django.db import models

class Drive(models.Model):
    device_path = models.CharField(max_length = 256)
    user_label = models.CharField(max_length = 32)
    manufacturer = models.CharField(max_length = 32)
    model = models.CharField(max_length = 64)
    terabytes = models.FloatField()
    install_date = models.DateField()

    def __str__(self):
        return self.user_label

class Attribute(models.Model):
    number = models.IntegerField()
    label = models.CharField(max_length = 128)

    def __str__(self):
        return self.label

class Value(models.Model):
    drive = models.ForeignKey(Drive, on_delete = models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete = models.CASCADE)
    date = models.DateTimeField()
    value = models.IntegerField()

    def __str__(self):
        return '<{}: {} = {} on {}>'.format(
            self.drive,
            self.attribute,
            self.value,
            self.date
        )
