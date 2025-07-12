from django.db import models

# Create your models here.

class Collage(models.Model):
    GRID_STYLE_CHOICES = [
        ('2x2', '2x2 Grid'),
        ('3x3', '3x3 Grid'),
        ('4x4', '4x4 Grid'),
        ('2x3', '2x3 Grid'),
        ('3x2', '3x2 Grid'),
        ('4x3', '4x3 Grid'),
        ('3x4', '3x4 Grid'),
    ]
    
    title = models.CharField(max_length=255)
    grid_style = models.CharField(max_length=10, choices=GRID_STYLE_CHOICES, default='3x3')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ImageItem(models.Model):
    collage = models.ForeignKey(Collage, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='collage_images/')

    def __str__(self):
        return f"Image for {self.collage.title}"
