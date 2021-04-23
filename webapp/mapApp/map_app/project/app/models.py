from django.db import models
from django.utils import timezone

class MapInfoModel(models.Model):
    name = models.CharField('店名',max_length=255,default='sample_name')
    genre = models.CharField('ジャンル',max_length=255,default='sample_genre')
    location = models.CharField('所在地',max_length=255,default='sample_location')
    lat = models.FloatField('経度',default=0)
    lng = models.FloatField('緯度',default=0)
    photo = models.ImageField(upload_to='documents/')
    created_at = models.DateField('登録日',default=timezone.now)




# Create your models here.
