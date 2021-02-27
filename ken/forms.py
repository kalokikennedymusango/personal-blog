from django import forms
from . models import update
from . models import Contacts

class updateForm(forms.ModelForm):
    class Meta:
        model = update
        fields =('content','date')

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('title','content','date')