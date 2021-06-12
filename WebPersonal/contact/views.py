from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def infoform (request) :
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid() :
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content') 
            number_phone = request.POST.get('number_phone')
            # procedemos a enviar el correo
            email = EmailMessage(
                "Web Personal: nuevo mensaje de correo",
                f"De {name} <{email}> \n\n Escribio: \n\n {content} y su numero telefonico es {number_phone}",
                "no-contestar@inbox.mailtrap.io",
                ["leonardo.almeidac@gmail.com"],
                reply_to=[email])
            try:
                email.send()
                return redirect(reverse('infodata')+'?ok')
            except :
                return redirect(reverse('infodata')+'?fail')
    
    return render(request, "contact/datos.html", {'form' : contact_form})
