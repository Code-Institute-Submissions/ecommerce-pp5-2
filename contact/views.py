from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def contact_form(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})
