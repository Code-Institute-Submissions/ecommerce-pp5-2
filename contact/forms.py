from django import forms
from .models import Contact
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'body',]
        captcha = ReCaptchaField()

        labels = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'body': 'Message',
        }
