from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .models import Collage, ImageItem
from .forms import CollageUploadForm

# Upload view
def upload_collage(request):
    if request.method == 'POST':
        form = CollageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            grid_style = form.cleaned_data['grid_style']
            
            collage = Collage.objects.create(
                title=title,
                grid_style=grid_style
            )
            
            # Handle multiple files from request.FILES
            images = request.FILES.getlist('images')
            if len(images) > 10:
                form.add_error('images', 'You can upload a maximum of 10 images.')
                return render(request, 'collage/upload.html', {'form': form})
            
            for img in images:
                ImageItem.objects.create(collage=collage, image=img)
            return redirect('collage_display', collage_id=collage.id)
    else:
        form = CollageUploadForm()
    return render(request, 'collage/upload.html', {'form': form})

# Display view
def collage_display(request, collage_id):
    collage = get_object_or_404(Collage, id=collage_id)
    images = collage.images.all()
    
    # Parse grid style to get columns
    grid_style = collage.grid_style
    if 'x' in grid_style:
        cols = int(grid_style.split('x')[0])
    else:
        cols = 3  # default
    
    return render(request, 'collage/display.html', {
        'collage': collage, 
        'images': images,
        'grid_cols': cols
    })

# List view
def collage_list(request):
    collages = Collage.objects.all().order_by('-created_at')
    return render(request, 'collage/list.html', {'collages': collages})

# Delete view
def delete_collage(request, collage_id):
    if request.method == 'POST':
        collage = get_object_or_404(Collage, id=collage_id)
        collage.delete()
        return redirect('collage_list')
    else:
        return redirect('collage_list')
