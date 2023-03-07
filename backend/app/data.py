from django.db import models
import uuid

def upload_path(instance, filename):
    return '/'.join(['image',str(instance.name), filename])


class genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name_genre
    
class Data(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    
    genre_movie = models.ForeignKey(genre,on_delete=models.CASCADE, related_name="genre_m")
    
    def __str__(self):
        return self.name

