from django.contrib import admin
from .models import *


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating']

