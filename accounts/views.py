from django.shortcuts import render, redirect 
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'You have been registered successfully')
                    return redirect('login')
                
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You have been successfully logout")
    return redirect('index')

def dashboard(request):
    user_contact = Contact.objects.all().filter(user_id=request.user.id)
    context = {
        'contacts':user_contact,
    }
    return render(request, 'accounts/dashboard.html', context)

# def delet(request, user_id, listing_id):
#     to_delete = Contact.objects.filter(user_id=request.user.id, listing_id=listing_id)
#     print(to_delete)
#     return redirect('dashboard')