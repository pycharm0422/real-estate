from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        realtor_email = request.POST['realtor_email']
        print(listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, username=username, email=email, phone=phone, message=message, user_id=user_id, realtor_email=realtor_email)

        contact.save()

        messages.success(request, 'Your response have been submitted. Realtor will get back to you soon')
    return redirect('/listing/'+listing_id)

def delet(request, user_id, listing_id):
    to_delete = Contact.objects.filter(user_id=request.user.id, listing_id=listing_id)
    print(to_delete)
    return redirect('dashboard')