from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        
        fields =[
           
            "add_keyword",
            
        ]
    
class KeywordListForm(forms.ModelForm):
    class Meta:
        model = Keyword
        
        fields =[
           
            "add_keyword",
            
        ]
class DetailForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields=["name","date"]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields=["update_d"]


class ManageForm(forms.ModelForm):
    class Meta:
        model = Dynamicques
        fields=["question"]