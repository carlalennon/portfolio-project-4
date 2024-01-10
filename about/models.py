from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ER About site 

# _______________
#|_ Title________|
#|_Admin icon____|  
#|_Admin name____|
#|_About content_|
#|_Date created__|
#|_______________|


class About(models.Model):
    title = models.CharField(max_length=300, unique=False)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="about_site"
    )
    # Icon for user
    # Content
    content = models.TextField()
    # Date and Time
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Creator: {self.author}"