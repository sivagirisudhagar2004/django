from django import forms

class MultipleFileInput(forms.FileInput):

        allow_multiple_selected = True

class MultipleFileField(forms.FileField):

    def __int__(self,*args,**kwargs):

        kwargs.setdefault("widget",MyImageForm(attrs={'class':'form-control'}))

        super().__init__(*args,**kwargs)

    def clean(self, data, initial = None):
        single_file_clean = super().clean
        if(isinstance(data,(list,tuple))):
            return [single_file_clean(d,initial) for d in data]
        return single_file_clean(data,initial)

class MyImageForm(forms.Form):

    file = MultipleFileField()