from django.db import models

# Create your models here.

#テーブル定義
class delayinfo(models.Model):
    linename = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    departurestation = models.CharField(max_length=30)
    arrivalstation = models.CharField(max_length=30)
    delaystatus = models.BooleanField(default=False)
    delayreason = models.TextField(blank=True, null=True)
    scrapedtime = models.DateTimeField(auto_now=True)

    #IDの代わりに日付データを返す
    def __str__(self):
        return self.date
    