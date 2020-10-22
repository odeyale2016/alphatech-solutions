from django import forms
from .models import Registerdb

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Registerdb
        fields = ('fullname','email','phone_number','company_name','message','date','position')
        labels = {'fullname': 'Full Name', 'email':'Email'}

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="Select"


