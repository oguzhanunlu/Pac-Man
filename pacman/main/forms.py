from django import forms

pchoices = (
    ('Ghost', 'Ghost'),
    ('Pacman', 'Pacman'),
)

class SignInForm(forms.Form):
    name = forms.CharField()


class SignUpForm(forms.Form):
    name = forms.CharField()
    ptype = forms.ChoiceField(choices=pchoices)