from django.db import models

# Create your models here.

'''
- Django 모델은 "django.db.models.Model" 의 파생 클래스
- 모델 클래스의 각 속성(Attribute)은 테이블의 필드에 해당
- 만약 Primary Key가 지정되지 않으면, DB 테이블 생성시 자동으로 id가 생성
- 각 Field 클래스마다 반드시 지정해야 주어야 하는 옵션이 있을 수 있는데, 예를 들어
  CharField (와 그 서브클래스들)은 필드의 최대 길이를 나타내는 max_length를 항상 지정해 주어야 한다.
'''

class Guestbook(models.Model):
    guestbook_id = models.AutoField(primary_key=True)
    guestbook_name = models.CharField(max_length=20)
    guestbook_text = models.TextField()