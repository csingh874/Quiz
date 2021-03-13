from django.db import models

# Create your models here.
class QtsAnsSet(models.Model):
    subject = models.CharField(max_length=100,null=True)
    question = models.CharField(max_length=250,null=True)
    opt1 = models.CharField(max_length=250,null=True)
    opt2 = models.CharField(max_length=250,null=True)
    opt3 = models.CharField(max_length=250,null=True)
    opt4 = models.CharField(max_length=250,null=True)
    answer = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.question