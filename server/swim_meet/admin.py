from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import SwimMeet  # using a relative import

# registering model to use in admin interface
admin.site.register(SwimMeet)
