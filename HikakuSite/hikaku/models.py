from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductModel(models.Model):
  name = models.CharField(verbose_name="商品名", max_length=100, default='')
  price = models.IntegerField(verbose_name="価格", default='')
  image_link = models.TextField(verbose_name="画像リンク", default='')
  
  def __str__(self) -> str:
    return self.name
        
class OfferModel(models.Model):
  product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
  price = models.IntegerField(verbose_name="価格", default='')
  shop = models.CharField(verbose_name="販売店", max_length=100, default='')
  shop_link = models.TextField(verbose_name="ショップリンク", default='')
  
  def __str__(self) -> str:
    return self.shop
  
class BookMarkModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return  str(self.id)