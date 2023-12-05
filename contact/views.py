from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def contact_form(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('products')
    else:
        contact_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})
