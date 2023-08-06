from django import template
from feedback.forms import *

register = template.Library()


@register.inclusion_tag("feedback/feedback_form.html")
def show_feedback_form(product_pk):
    feedback_form = AddFeedbackForm()
    context = {
        "feedback_form": feedback_form,
        "product_pk": product_pk,
    }
    return context


@register.inclusion_tag("feedback/feedback-stars.html")
def show_feedback_stars(average_rating, show_counter=False, counter=0):
    context = {
        "average_rating": float(average_rating),
        "show_counter": show_counter,
        "counter": counter,
    }
    return context
