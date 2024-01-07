from django.db import models
from django.contrib.auth.models import User

# Create your models here.
## Forum model - Board ER table - * = Forgein key
# _________________
#|_ID______________|      
#|_Thread Name_____|
#|_Creator_________|*
#|_Creator icon____|
#|_Creator bio_____|
#|_Date____________|
#|_no. Replies_____|
#|_Pinned status___|
#|_Tags____________|
#|_Content_________|
#|_Time____________|
#|_no. Views_______|
#|_Replies_________|

# Much of this is lifted from the LMS

STATUS = ((0, "Draft"), (1, "Published"))

class Thread(models.Model):
    #Thread title
    title = models.CharField(max_length=500, unique=True)
    #Creates url for post - replace with number in future
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # Text post
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)