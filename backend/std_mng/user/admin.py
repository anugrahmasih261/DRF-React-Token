from django.contrib import admin
from .models import User
# admin.py
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

admin.site.register(User)
# admin.site.register(OutstandingToken)
