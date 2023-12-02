from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def contact_form(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirct('success_url')
    
    return render(request, 'contact.html', {'contact_form': contact_form})