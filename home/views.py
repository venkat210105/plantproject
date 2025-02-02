from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import ImageUploadForm
from django.conf import settings
import os

def index(request):
    #return HttpResponse("V")
    context={
        'variable':'Jai Ganesha'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Ensure the uploads directory exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # Save the file to the MEDIA_ROOT directory
            image = form.cleaned_data['image']
            upload_path = os.path.join(settings.MEDIA_ROOT, image.name)
            print(f"Saving image to: {upload_path}")  # Debugging: Print the file path

            with open(upload_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            return render(request, 'upload.html', {'form': form, 'success_message': 'File uploaded successfully!', 'image_url': os.path.join(settings.MEDIA_URL, image.name)})
        else:
            # Render the template with form errors
            return render(request, 'upload.html', {'form': form})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})