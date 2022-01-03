from django.db import models

class AbstractModel(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class UserInput(AbstractModel):
    age = models.IntegerField(default=18)

class Feedback(AbstractModel):
    pass