from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    RATING_CHOICES = [(i, f"{i} stars") for i in range(1, 6)]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'rating-input'}),
        label='Rating'
    )
    
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email (optional)'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your thoughts on this artwork...', 'rows': 4}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Email (optional)',
            'comment': 'Comment',
        }
