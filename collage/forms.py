from django import forms
from .models import Collage, ImageItem

class CollageForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)

    class Meta:
        model = Collage
        fields = ['title', 'images']

    def clean_images(self):
        images = self.files.getlist('images')
        if len(images) > 10:
            raise forms.ValidationError('You can upload a maximum of 10 images.')
        return images
