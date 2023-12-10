from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

# Create your views here.


def contact_form(request):
    '''
    A contact form for the custemor to contact the business.
    An email is sent to the site owner to notify them that a customer has sent
    contact email. And an email is sent to the client to confirm reciept of email.
    The contact email is saved in the admin panel.
    The site check if the user is logged and prepopulates the contact form with the users 
    details
    '''

    # Check if user is logged and add users details into the form

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        initial_data = {
            'name': profile.user.get_full_name(),
            'email': profile.user.email,
        }
        contact_form = ContactForm(initial=initial_data)
    else:
        contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Get the form data
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['body']

            # Send site owner an email
            site_subject = f'New email from {name}'
            site_message = f'Subject: {subject}\nFrom: {name} <{email}>\n\n{message}'

            send_mail(
                site_subject,
                site_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                )

            # Send the user a confirmation email

            subject = render_to_string(
                'contact_emails/email_confirmation_subject.txt', {'name': name})
            body = render_to_string(
                'contact_emails/email_confirmation_body.txt', {'name': name})
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [email,]
                )
            
            # Send a success message
            messages.info(request, 'Message sent. We will be in contact with you as soon as possible')
            return redirect('products')

    return render(request, 'contact.html', {'contact_form': contact_form})
