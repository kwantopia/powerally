from django import forms

class CustomerForm(forms.Form):
  email = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
  zip_code = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder':'Zipcode'}))
  account_number = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'placeholder':'Account #'}))
