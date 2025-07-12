from django.shortcuts import render, redirect, get_object_or_404
from .models import Collage, ImageItem
from .forms import CollageForm

def collage_list(request):
    collages = Collage.objects.all().order_by('-created_at')
    return render(request, 'collage/list.html', {'collages': collages})

def collage_upload(request):
    if request.method == 'POST':
        form = CollageForm(request.POST, request.FILES)
        if form.is_valid():
            collage = form.save()
            images = request.FILES.getlist('images')
            for img in images:
                ImageItem.objects.create(collage=collage, image=img)
            return redirect('collage_display', collage_id=collage.id)
    else:
        form = CollageForm()
    return render(request, 'collage/upload.html', {'form': form})

def collage_display(request, collage_id):
    collage = get_object_or_404(Collage, id=collage_id)
    images = collage.images.all()
    return render(request, 'collage/display.html', {'collage': collage, 'images': images})
