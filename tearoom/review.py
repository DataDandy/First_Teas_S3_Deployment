from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewer_name', 'menu_items', 'review_title', 'stars', 'comment', 'review_image', 'status')
