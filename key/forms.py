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
        widgets = {
            'add_keyword':forms.TextInput(attrs={'placeholder':'Enter Keyword'}),
        }
    
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
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter Presentation name'}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields=["update_d"]


class ManageForm(forms.ModelForm):
    class Meta:
        model = Dynamicques
        fields=["question"]

        widgets = {
            'question':forms.TextInput(attrs={'placeholder':'Enter question'}),
        }