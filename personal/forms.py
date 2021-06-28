from .models import InterestedPeople
from django import forms

class InterestedPeopleForm(forms.ModelForm):
    class Meta:
        model =  InterestedPeople
        fields =['email','name','animalname','address','number','whatsapp','instagram','facebook']