from django import forms


class NewDogTagForm(forms.Form):
    owner_name = forms.CharField()
    dog_name = forms.CharField()
    dog_birthday = forms.DateField()


class NewCatTagForm(forms.Form):
    owner_name = forms.CharField()
    cat_name = forms.CharField()
    cat_birthday = forms.DateField()
