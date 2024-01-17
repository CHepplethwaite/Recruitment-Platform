from django.db import models
from django.urls import reverse
from PIL import Image
    
class organisation(models.Model):
    organisation_name = models.CharField(max_length=200)
    organisation_code = models.CharField(max_length=200)
    organisation_description = models.TextField()
    organisation_website = models.CharField(max_length=200)
    organisation_logo = models.ImageField(upload_to='media/logos', default='default_logo.png')
    
    def __str__(self):
        return self.organisation_name
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    
    
    
