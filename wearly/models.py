from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


# 유저 정보(이름, 성별, 나이, 이미지별 점수)
class User(models.Model):
    # def __init__(self):
    #     =__init__.abc
    idx = models.BigAutoField(settings.AUTH_USER_MODEL, primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=3)
    age = models.IntegerField()
    imageScore1 = models.TextField()
    imageScore2 = models.TextField()
    imageScore3 = models.TextField()
    imageScore4 = models.TextField()
    imageScore5 = models.TextField()
    imageScore6 = models.TextField()
    imageScore7 = models.TextField()
    imageScore8 = models.TextField()
    imageScore9 = models.TextField()
    imageScore10 = models.TextField()
    imageScore11 = models.TextField()
    imageScore12 = models.TextField()
    imageScore13 = models.TextField()
    imageScore14 = models.TextField()
    imageScore15 = models.TextField()
    imageScore16 = models.TextField()
    imageScore17 = models.TextField()
    imageScore18 = models.TextField()
    imageScore19 = models.TextField()
    imageScore20 = models.TextField()
    imageScore21 = models.TextField()
    imageScore22 = models.TextField()
    imageScore23 = models.TextField()
    imageScore24 = models.TextField()
    imageScore25 = models.TextField()
    imageScore26 = models.TextField()
    imageScore27 = models.TextField()
    imageScore28 = models.TextField()
    imageScore29 = models.TextField()
    imageScore30 = models.TextField()
    imageScore31 = models.TextField()
    imageScore32 = models.TextField()
    imageScore33 = models.TextField()
    imageScore34 = models.TextField()
    imageScore35 = models.TextField()
    imageScore36 = models.TextField()
    imageScore37 = models.TextField()
    imageScore38 = models.TextField()
    imageScore39 = models.TextField()
    imageScore40 = models.TextField()
    imageScore41 = models.TextField()
    imageScore42 = models.TextField()
    imageScore43 = models.TextField()
    imageScore44 = models.TextField()
    imageScore45 = models.TextField()
    imageScore46 = models.TextField()
    imageScore47 = models.TextField()
    imageScore48 = models.TextField()
    imageScore49 = models.TextField()
    imageScore50 = models.TextField()
    imageScore51 = models.TextField()
    imageScore52 = models.TextField()
    imageScore53 = models.TextField()
    imageScore54 = models.TextField()
    imageScore55 = models.TextField()
    imageScore56 = models.TextField()
    imageScore57 = models.TextField()
    imageScore58 = models.TextField()
    imageScore59 = models.TextField()
    imageScore60 = models.TextField()
    imageScore61 = models.TextField()
    imageScore62 = models.TextField()
    imageScore63 = models.TextField()
    imageScore64 = models.TextField()
    imageScore65 = models.TextField()
    imageScore66 = models.TextField()
    imageScore67 = models.TextField()
    imageScore68 = models.TextField()
    imageScore69 = models.TextField()
    imageScore70 = models.TextField()
    imageScore71 = models.TextField()
    imageScore72 = models.TextField()
    imageScore73 = models.TextField()
    imageScore74 = models.TextField()
    imageScore75 = models.TextField()
    imageScore76 = models.TextField()
    imageScore77 = models.TextField()
    imageScore78 = models.TextField()
    imageScore79 = models.TextField()
    imageScore80 = models.TextField()
    imageScore81 = models.TextField()
    imageScore82 = models.TextField()
    imageScore83 = models.TextField()
    imageScore84 = models.TextField()
    imageScore85 = models.TextField()
    imageScore86 = models.TextField()
    imageScore87 = models.TextField()
    imageScore88 = models.TextField()
    imageScore89 = models.TextField()
    imageScore90 = models.TextField()
    imageScore91 = models.TextField()
    imageScore92 = models.TextField()
    imageScore93 = models.TextField()
    imageScore94 = models.TextField()
    imageScore95 = models.TextField()
    imageScore96 = models.TextField()
    imageScore97 = models.TextField()
    imageScore98 = models.TextField()
    imageScore99 = models.TextField()
    imageScore100 = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    # return self.gender

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()


# 이미지 사진(파일 이름)
class Image(models.Model):
    idx = models.BigAutoField(primary_key=True)
    file = models.ImageField(upload_to='', blank=False)

    # def __str__(self):
    #     return self.file
