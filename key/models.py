from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
# Create your models here.
class Keyword(models.Model):
    
    add_keyword = models.CharField(max_length=120, blank=True, null=True)
    
    def __str__(self):
        return "{add_keyword}" .format(add_keyword=self.add_keyword)

# class Answer(models.Model):
#     keyword=models.ForeignKey(Keyword, on_delete=models.SET_NULL, blank=True, null=True)
#     question = models.CharField(max_length=2000, null=True, blank=True)
#     answer = models.CharField(max_length=2000, null=True, blank=True)
    

#     def __str__(self):
#         return "{question}-{answer}" .format(question=self.question, answer=self.answer)

class Presentation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return "{name}-{date}" .format(name=self.name, date=self.date)

class Detail(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.SET_NULL, blank=True, null=True)
    update_d = models.DateField(("Date"), default=datetime.date.today)
    title = models.CharField(max_length=64, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    presentation = models.ForeignKey(Presentation, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{title}-{description}" .format(title=self.title, description=self.description)

class Dynamicques(models.Model):
    question = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return "{question}" .format(question=self.question)