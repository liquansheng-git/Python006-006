from django.db import models

# Create your models here.
class DouBanFilmReview(models.Model):
    '''豆瓣影评类'''
    # 豆瓣用户名
    doubanusername = models.CharField(max_length=200)
    # 星级数
    doubangradestar = models.IntegerField(default=0)
    # 短评有用数
    doubangradeUserflunumber = models.IntegerField(default=0)
    # 短评内容
    doubangradecontent = models.CharField(max_length=1500)

    def __str__(self):
        return self.doubanusername
    
    class Meta:
        db_table = 'doubanfilmreview'


    
