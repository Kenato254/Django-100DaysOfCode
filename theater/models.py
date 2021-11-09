import uuid
import datetime
from django.db import models
from django.db.models.fields import BooleanField
from django.utils import timezone
from django.db.models.expressions import Value
from django.db.models.functions import Concat


# class TheaterModel(models.Model):
#     name = models.CharField(max_length=50)
#     contact = models.CharField(max_length=50, default="")
#     address = models.CharField(max_length=100, default="")
#     location = models.CharField(max_length=100)
#     now_showing = models.DateTimeField(auto_now=True)
#     # Relationships

#     def __str__(self):
#         return self.name

# class MovieModel(models.Model):
#     title = models.CharField(max_length=100)
#     ratings = models.IntegerField()
#     genre = models.CharField(max_length=100)
#     description = models.TextField()
#     poster = models.ImageField(upload_to="movie/posters/%Y/%M/%d", null=True, blank=True)
#     release_date = models.DateTimeField()
#     # Relationships
#     trailer = models.OneToOneField("TrailerModel", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class TrailerModel(models.Model):
#     caption = models.CharField(max_length=200)
#     file = models.FileField(upload_to="movie/trailers/%Y/%M/%d", null=True, blank=True)
#     url = models.URLField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.caption

# class CustomerModel(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     email = models.EmailField()
    
#     def __str__(self) -> str:
#         return self.email

# class TicketModel(models.Model):
#     ticket_number = models.UUIDField("Ticket Number", default=uuid.uuid4)
#     customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
#     movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
#     seat = models.OneToOneField("SeatModel", on_delete=models.CASCADE)
#     cinemax = models.ForeignKey(
#         TheaterModel, 
#         null=True, 
#         blank=True, 
#         on_delete=models.SET_NULL
#     )
#     def __str__(self):
#         return f'''
#         Ticket for {self.customer}
#         '''

# class SeatModel(models.Model):
#     FRONT_LEFT = "FL"
#     FRONT_MIDDLE = "FM"
#     FRONT_RIGHT = "FR"
#     MID_LEFT = "ML"
#     MID_MIDDLE = "MM"
#     MID_RIGHT  = "MR"
#     BACK_LEFT = "BL"
#     BACK_MIDDLE = "BM"
#     BACK_RIGHT  = "BR"

#     SEAT_POSITION_CHOICES = [
#         (FRONT_LEFT, "FL"),        
#         (FRONT_MIDDLE, "FM"),
#         (FRONT_RIGHT, "FR"),   
#         (MID_LEFT, "ML"),
#         (MID_MIDDLE, "MM"),
#         (MID_RIGHT , "MR"),    
#         (BACK_LEFT, "BL"),        
#         (BACK_MIDDLE, "BM"),
#         (BACK_RIGHT, "BR"),        
#     ]
#     seat_number = models.IntegerField(default=87)
#     seat_position = models.CharField(max_length=2, choices=SEAT_POSITION_CHOICES, default="SELECT SEAT")

#     def __str__(self):
#         return self.seat_position

class CountryModel(models.Model):
    name = models.CharField(max_length=255, default="")
    independent = models.CharField(max_length=4, null=True)

    def __str__(self):
        return self.name

class CityModel(models.Model):
    name = models.CharField(max_length=50, default="")
    population = models.IntegerField()
    jobs = models.IntegerField()
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name

class PersonQuerySet(models.QuerySet):
    """Add annotations to Managers or QuerySet"""
    def annotate_full_name(self):
        """ Creates a dynamic field -> `full_name` and returns it in a QuerySet """
        return self.annotate(
            full_name = Concat(
                'first_name', Value(' '), 'last_name'
            )
        )
class PersonModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(default=timezone.now)
    age = models.IntegerField(default=25)
    job = models.CharField(max_length=100, default="")
    last_donated = models.DateTimeField(default=datetime.datetime.today()-datetime.timedelta(5))
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    personal = models.UUIDField("Personal Identification Number", default=uuid.uuid4)
    marital_status = models.JSONField(default=dict(MaritalStatus= "Single"))
    pet = models.JSONField(null=True)

    objects = PersonQuerySet.as_manager()

    @property
    def pin(self):
        return self.personal

    def __str__(self):
        return self.first_name
        
class SearchModel(models.Model):
    search_bar = models.CharField(max_length=50)
    by_country = models.BooleanField(default=False)
    by_age = models.BooleanField(default=False)
    by_job = models.BooleanField(default=False)
    
class DogModel(models.Model):
    name = models.CharField(max_length=20)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
    