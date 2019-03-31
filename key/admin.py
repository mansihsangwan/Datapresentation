from django.contrib import admin

# Register your models here.
from key.models import *
class KeywordModelAdmin(admin.ModelAdmin):
    display=('add_keyword')
    
    class Meta:
         model = Keyword

class PresentationModelAdmin(admin.ModelAdmin):
    display=('name','date')
    
    class Meta:
         model = Presentation

class DetailModelAdmin(admin.ModelAdmin):
    display=('title','description')
    
    class Meta:
         model = Detail

admin.site.register(Keyword, KeywordModelAdmin)
# admin.site.register(Answer, AnswerModelAdmin)
admin.site.register(Presentation)
admin.site.register(Detail)
admin.site.register(Dynamicques)
