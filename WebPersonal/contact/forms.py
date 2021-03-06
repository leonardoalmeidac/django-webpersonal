from django import forms

class ContactForm(forms.Form) :
    name = forms.CharField(label = 'Nombre', required = True)
    email = forms.EmailField(label = 'Email', required = True)
    content = forms.CharField(label = 'Mensaje', required = True, widget=forms.Textarea)
    number_phone = forms.CharField(label = 'N. Telefónico', required = True)