from django.db import models


class CartInfo(models.Model):
    user = models.ForeignKey('df_user.UserInfo',on_delete=models.CASCADE)
    good = models.ForeignKey('df_goods.GoodInfo',on_delete=models.CASCADE)
    count = models.IntegerField()