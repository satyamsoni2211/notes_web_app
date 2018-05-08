from django import forms
from .models import Notes

class MyModelForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('title','text')

        widgets = {
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea  form-horizontal postcontent'})
            }