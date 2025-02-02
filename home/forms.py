from django import forms
from django.core.exceptions import ValidationError

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            file_size_kb = image.size / 1024  # Convert bytes to KB
            if file_size_kb < 15 or file_size_kb > 50:
                raise ValidationError('Image size must be between 15KB and 50KB.')
        return image