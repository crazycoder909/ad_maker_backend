from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

class ad(models.Model):
    # Campaign
    campaignName = models.CharField(max_length=255)
    
    # AdSet
    adsetName = models.CharField(max_length=255)
    # gender = ArrayField(models.IntegerField(), blank=True, null=True, help_text="Indexes of selected genders")
    # age = ArrayField(models.IntegerField(), blank=True, null=True, help_text="Indexes of selected genders")
    dailyBudget = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    bidRate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    frequencyCap = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)])
    
    # Ads
    # Single image
    adName = models.CharField(max_length=255)
    adType = models.CharField(max_length=100)
    titleS = models.TextField()
    imageS = models.ImageField(upload_to='assets/images/', null=True, blank=True, default = None)
    descS = models.TextField()
    textS = models.CharField(max_length=255)
    brandS = models.TextField()
    logoS = models.ImageField(upload_to='assets/images/', null=True, blank=True, default = None)
    urlS = models.TextField()
    
    # Carousel ads
    logoC = models.ImageField(upload_to='assets/images/', null=True, blank=True)    
    brandC = models.TextField()
    primaryC = models.TextField()
    seeC = models.TextField()

    # Video
    titleV = models.TextField()
    videoV = models.FileField(upload_to='assets/videos/', null=True, blank=True, default = None)
    imageV = models.ImageField(upload_to='assets/images/', null=True, blank=True, default = None)
    descV = models.TextField()
    textV = models.CharField(max_length=255)
    brandV = models.TextField()
    logoV = models.ImageField(upload_to='assets/images/', null=True, blank=True, default = None)
    urlV = models.TextField()
