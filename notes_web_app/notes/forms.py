from django import forms
from .models import Notes

class MyModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs = {
            'class': 'editable',
            'type': 'textbox'
        }

    class Meta:
        model = Notes
        fields = ('title','text')