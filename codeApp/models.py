from django.utils.timezone import now
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.user.username

class Author(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField('BookModel')
    published = models.IntegerField(default=0)
    data = models.JSONField(null=True)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('jSon:authors-list')
        
    class Meta:
        ordering = ['name']

class BookModel(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=now)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True, 
        on_delete=models.SET_NULL
    )
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
  

def post_save_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
post_save.connect(post_save_created_signal, sender=User)

