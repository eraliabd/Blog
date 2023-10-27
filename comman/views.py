from django.shortcuts import render
from .models import ContactInfo, ContactRequest, About


def contact_info(request):
    contact_information = ContactInfo.objects.first()

    context = {
        "contact_info": contact_information
    }
    return render(request, 'contact.html', context=context)


def contact(request):
    if request.method == 'POST':
        model = ContactRequest()
        model.name = request.POST.get('name', '')
        model.email = request.POST.get('email', '')
        model.subject = request.POST.get('subject', '')
        model.message = request.POST.get('message', '')

        model.save()

    return render(request, 'contact.html')


def about_info(request):
    about_info = About.objects.first()

    context = {
        "about_info": about_info
    }
    return render(request, 'about.html', context=context)
