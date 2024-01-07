from django.db import models
from django.contrib.auth.models import User

# Create your models here.
## Forum model - Board ER table - * = Forgein key
# _________________
#|_ID______________|   -   
#|_Thread Name_____|   -
#|_Creator_________|*  -
#|_Creator icon____|   X
#|_Creator bio_____|   X
#|_Date____________|   -
#|_no. Replies_____|   X
#|_Pinned status___|   -
#|_Tags____________|   -
#|_Content_________|   -
#|_Time____________|   -
#|_no. Views_______|   X
#|_Replies_________|   X

# Much of this is lifted from the LMS

STATUS = ((0, "Draft"), (1, "Published"))
PINNED = ((0, "Unpinned"), (1, "Pinned"))
TAGS = ((0, "General"), (1, "Pattern"), (2, "Yarn"), (3, "Technique"))

class Thread(models.Model):
    #Thread title
    threadname = models.CharField(max_length=500, unique=True)
    #Creates url for post - replace with number in future
    postID = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # Add icon for user
    # Add no. of replies
    # Pinned post
    pinned = models.IntegerField(choices=PINNED, default=0)
    # Tags - could later be used to define board
    tags = models.IntegerField(choices=TAGS, default=0)
    # Text post
    content = models.TextField()
    # Date and Time
    created_on = models.DateTimeField(auto_now_add=True)
    # Draft
    status = models.IntegerField(choices=STATUS, default=0)