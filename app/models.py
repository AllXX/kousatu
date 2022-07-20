from django.db import models
from datetime import datetime

# Create your models here.
"""
class Dbtest(models.Model):
    text = models.CharField(max_length=100)
    number = models.IntegerField()
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.text} ,{self.number} ,{self.name}'
"""
class Thread(models.Model):
    #タイトル
    title = models.CharField('タイトル',max_length=200,blank=False)
    #メッセージ
    message = models.TextField('メッセージ',blank=False)
    #登録日時
    pub_data = models.DateTimeField('登録日時',auto_now_add=True,editable=False)

    class Meta:
        verbose_name_plural = 'スレッド'
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    #スレッド
    title = models.ForeignKey(Thread,verbose_name='スレッド',on_delete=models.CASCADE)
    #メッセージ
    message = models.CharField('メッセージ',max_length=200, blank=False)
    #登録日時
    pub_data = models.DateTimeField('登録日時',auto_now_add=True,editable=False)

    class Meta:
        verbose_name_plural = 'コメント'
        ordering = ('title', ) # nameで昇順ソート
    
    def __str__(self):
        return '{} {}'.format(self.title, self.message)