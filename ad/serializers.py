from .models import ad
from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator

class AdSerializer(serializers.ModelSerializer):
    # Campaign
    campaignName = serializers.CharField(max_length=255, required=False)
    
    # AdSet
    adsetName = serializers.CharField(max_length=255, required=False)
    # gender = serializers.ListField(child=serializers.IntegerField(), help_text="Indexes of selected genders", required=False)
    # age = serializers.ListField(child=serializers.IntegerField(), help_text="Indexes of selected ages", required=False)    
    dailyBudget = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)],required=False)
    bidRate = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)], required=False)
    frequencyCap = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000)], required=False)
    
    # Ads
    # Single image
    adName = serializers.CharField(max_length=255, required=False)
    adType = serializers.CharField(max_length=100, required=False)
    titleS = serializers.CharField(required=False)
    imageS = serializers.ImageField(required=False)
    descS = serializers.CharField(required=False)
    textS = serializers.CharField(max_length=255, required=False)
    brandS = serializers.CharField(required=False)
    logoS = serializers.ImageField(required=False)
    urlS = serializers.CharField(required=False)
    
    # Carousel ads
    logoC = serializers.ImageField(required=False)    
    brandC = serializers.CharField(required=False)
    primaryC = serializers.CharField(required=False)
    seeC = serializers.CharField(required=False)

    # Video
    titleV = serializers.CharField(required=False)
    videoV = serializers.FileField(required=False)
    imageV = serializers.ImageField(required=False)
    descV = serializers.CharField(required=False)
    textV = serializers.CharField(max_length=255, required=False)
    brandV = serializers.CharField(required=False)
    logoV = serializers.ImageField(required=False)
    urlV = serializers.CharField(required=False)

    class Meta:
        model = ad
        fields = "__all__"  # Adjust as necessary