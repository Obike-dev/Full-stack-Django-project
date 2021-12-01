from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from shoes_app.models import Shoe

GENDER = [ ('Male', 'Male'), ('Female', 'Female'), ('not specified', 'Rather not say') ]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/user_profile_images/user_{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)   
    image = ResizedImageField(size=[320, 320], quality=99,
    crop=['middle', 'center'],
    upload_to=user_directory_path, 
    blank=True, null=True,
    default='users/user_default_img.png'
    )
    bio = models.TextField(blank=True)
    website = models.URLField(max_length=30,blank=True)
    gender = models.CharField(max_length=13,choices=GENDER,null=True)
    
    def __str__(self) -> str:
        return self.user.username


    







