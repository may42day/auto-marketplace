from django.http import HttpResponseRedirect
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
    url = feedback.product.get_absolute_url()
    return HttpResponseRedirect(f"{url}")


@login_required
def remove_feedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    url = feedback.product.get_absolute_url()
    feedback.calculate_average_rating(delete=True, exclude_pk=feedback.pk)
    if request.user == feedback.user:
        feedback.delete()

    return HttpResponseRedirect(f"{url}")
