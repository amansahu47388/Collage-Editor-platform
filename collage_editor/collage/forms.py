from django import forms
from .models import Collage, ImageItem

class CollageForm(forms.ModelForm):
    class Meta:
        model = Collage
        fields = ['title', 'grid_style']

class ImageItemForm(forms.ModelForm):
    class Meta:
        model = ImageItem
        fields = ['image']

class CollageUploadForm(forms.Form):
    title = forms.CharField(max_length=255)
    grid_style = forms.ChoiceField(
        choices=Collage.GRID_STYLE_CHOICES,
        initial='3x3',
        widget=forms.RadioSelect,
        help_text="Choose your grid layout"
    )
    images = forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'image/*'}),
        required=False
    )
