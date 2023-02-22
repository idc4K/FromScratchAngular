from django.db import models
import uuid

class genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name_genre
    
class Data(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    image = models.FileField(upload_to='image_movie/', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    
    genre_movie = models.ForeignKey(genre,on_delete=models.CASCADE, related_name="genre_m")
    
    def __str__(self):
        return self.name

