from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

#슬랙에서 받는 정보들..
'''
1. 유저
2. 날짜
3. 메세지
4. commit 숫자 (?)
5. commit 메세지
6. 레포지토리 이름
7. 레포지토리 링크
'''
class OutGoingSlack(models.Model):
    author = models.CharField(max_length=100)
    publish_date = models.DateTimeField(blank=True, null=True)
    msg = models.TextField() #커밋 메세지
    indexOfCommit = models.CharField(max_length=100)
    commitUrl = models.TextField()
    repository = models.CharField(max_length=100)
    repositoryUrl = models.TextField()


    def publish(self):
        self.publish_date = timezone.now()

    def __str__(self):
        return self.msg
