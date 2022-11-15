from .models import Feedback
from django.forms import ModelForm, Textarea, Select


class AddFeedbackForm(ModelForm):

    class Meta:
        model = Feedback
        fields = ('rating', 'text')
        widgets = {
            'rating': Select(attrs={
                'placeholder': 'Select rating',
                'class': 'form-select form-select-lg',
            }),
            'text': Textarea(attrs={
                'placeholder': 'Review text',
                'class': 'form-control',
                'rows': '3',
            }),
        }
