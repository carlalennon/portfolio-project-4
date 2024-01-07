from django.db import models

# Create your models here.
## Forum model - Board ER table - * = Forgein key
# _________________
#|_ID______________|      
#|_Thread Name_____|
#|_Creator_________|*
#|_Date____________|
#|_no. Replies_____|
#|_Pinned status___|
#|_Tags____________|
#|_Content_________|
#|_Time____________|
#|_no. Views_______|
#|_Replies_________|