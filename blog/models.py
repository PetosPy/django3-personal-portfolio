from django.db import models

# Create your models here.
class Blog(models.Model):

    title= models.CharField(max_length=100) 
    description = models.TextField()
    added_on = models.DateField()

    # Show real names in db
    def __str__(self):
        return self.title
    
    

    # image = models.ImageField(upload_to="portfolio/images/")
    # url = models.URLField(blank=True)
