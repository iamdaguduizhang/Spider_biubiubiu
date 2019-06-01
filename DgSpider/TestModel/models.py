# Create your models here.

from django.db import models


class Test(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    search_engine = models.CharField(max_length=20)
    keyword_search = models.CharField(max_length=20)
    page_num = models.IntegerField()
    status = models.IntegerField(default=1)
