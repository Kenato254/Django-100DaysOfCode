from django.contrib import admin

from .models import BookModel, User, UserProfile, Author

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(BookModel)
admin.site.register(Author)