from django import forms

TYPE_CHOICE=(('Ghost','Ghost'),('Pacman','Pacman'))

class signinform(forms.Form):
    name=forms.CharField()

class signupform(forms.Form):
    name=forms.CharField()
    ptype=forms.ChoiceField(choices=TYPE_CHOICE)