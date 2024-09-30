from django.db import models

from users.models import CustomUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    cover_pic = models.ImageField(upload_to='books/cover_pics/', null=True, blank=True)
    pdf_file= models.FileField(upload_to='books/pdf_files/', null=True, blank=True)
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books_created')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
