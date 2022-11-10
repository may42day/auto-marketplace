from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import AddFeedbackForm
from goods.models import Product
from .models import Feedback

@require_POST
@login_required
def add_feedback(request, product_id):
    feedback_form = AddFeedbackForm(request.POST)
    feedback = feedback_form.save(commit=False)
    feedback.user = request.user
    product = Product.objects.get(pk=product_id)
    feedback.product = product
    feedback.save()
    avg_rating = round(Feedback.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg'],1)
    product.average_rating = avg_rating
    url = product.get_absolute_url()
    product.save()
    return HttpResponseRedirect(f'{url}')



@login_required
def remove_feedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    product = feedback.product
    url = feedback.product.get_absolute_url()
    if request.user == feedback.user:
        feedback.delete()

    avg_rating = round(Feedback.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg'], 1)
    product.average_rating = avg_rating
    product.save()
    return HttpResponseRedirect(f'{url}')
