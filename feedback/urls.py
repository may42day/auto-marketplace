from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/<int:product_id>', add_feedback, name='add_feedback'),
    path('remove/<int:product_id>/<int:feedback_id>', remove_feedback, name='remove_feedback'),

    ]


