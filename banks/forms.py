from django import forms

class IFSCForm(forms.Form):
    IFSC = forms.CharField(max_length = 11, required=True)
   
class BANKSForm(forms.Form):
    BANKNAME = forms.CharField(max_length = 49, required=True, widget=forms.Textarea)
    CITYNAME = forms.CharField(max_length = 50, required=True, widget=forms.Textarea)
    