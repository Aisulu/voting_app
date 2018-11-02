from django.contrib import admin

from .models import Tweet
from .models import Vote

admin.site.register(Tweet)
admin.site.register(Vote)
