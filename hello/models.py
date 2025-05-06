from django.db import models

class ArtPiece(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='art_images/')
    year_created = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ added field for sorting

    def __str__(self):
        return self.title

class Feedback(models.Model):
    art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} on {self.art_piece}'
