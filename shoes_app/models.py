from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.utils.text import slugify

import string
import random


def shoe_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'shoes_app/shoe_images/user_{0}/{1}'.format(instance.user.id, filename)


GENDER = [ ('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex') ]
CATEGORY = [ ('Boots', 'Boots'), ('Sneakers', 'Sneakers'), 
('Sports', 'Sports'), ('Men','Men'), ('Women','Women') ]


class Shoe(models.Model): 
    slug = models.SlugField(allow_unicode=True,unique=True,blank=True)
    name = models.CharField(max_length=25)
    brand = models.CharField(max_length=20,blank=True)
    description = models.TextField()
    price = models.FloatField(blank=True,null=True,default=0)
    shoe_size = models.FloatField(null=True,blank=True)
    category = models.CharField(max_length=10,choices=CATEGORY)
    gender =  models.CharField(max_length=6,choices=GENDER)
    posted_at = models.DateField(default= datetime.now,blank=True,null=True)
    time_posted = models.TimeField(default=timezone.now,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    shop_name = models.CharField(max_length=50,blank=True)
    about_shop = models.TextField(blank=True) 
    website = models.URLField(max_length=50,blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    facebook = models.CharField(max_length=30,blank=True)
    twitter = models.CharField(max_length=30,blank=True)


    image1 = models.ImageField(
    upload_to=shoe_directory_path, 
    default=''     
    )

    image2 = models.ImageField(
    upload_to=shoe_directory_path,
    blank=True,null=True,
    default=''    
    )
    image3 = models.ImageField(
    upload_to=shoe_directory_path,
    blank=True,null=True,
    default=''    
    )
    image4 = models.ImageField(
    upload_to=shoe_directory_path,
    blank=True,null=True,
    default=''    
    )

    image5 = models.ImageField(
    upload_to=shoe_directory_path,
    blank=True,null=True,
    default=''    
    )

    def __str__(self) -> str:
        return self.name
    
    def rand_slug(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.rand_slug() + "-" + self.name)
        super(Shoe, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("shoes_app:shoe_detail", kwargs={"slug":self.slug})
    








    
    

 
