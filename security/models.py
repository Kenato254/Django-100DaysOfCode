from django.db import models

class UserInput(models.Model):
    name = models.CharField(max_length=500)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name
    
