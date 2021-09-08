from django.db import models

# Create your models here.

class Question(models.Model): # clas = 함수들을 저장해놓는 주머니
    subject = models.CharField(max_length = 200)#제목
    content = models.TextField()#글
    create_date = models.DateTimeField()#작성 날짜(시간)

    def __str__(self):
        return self.subject
            #항상 제목이 보이도록 설정

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # 작성자가 질문을 샂게하면 답변도 함께 사라진다
    content = models.TextField()
    create_date = models.DateTimeField()