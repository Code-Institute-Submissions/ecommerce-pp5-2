from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.


def contact_form(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            ''' Get the form data'''
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['body']

            ''' Send the email to the site email address'''

            send_mail(
                subject,
                message,
                email,
                [settings.EMAIL_HOST_USER],
            )

            ''' Send the user a confirmation email'''

            subject = render_to_string(
                'contact_emails/email_confirmation_subject.txt', {'name': name})
            body = render_to_string(
                'contact_emails/email_confirmation_body.txt')
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [email,]
                )
            
           
            # send_mail(
            #     'Thank you for contacting us',
            #     f"Dear {name}, we have recieved your message and will get back you shortly.",
            #     email,
            #     [email],
            #     )

            # Send a success message
            messages.info(request, 'Message sent')
            return redirect('products')
    else:
        contact_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})
