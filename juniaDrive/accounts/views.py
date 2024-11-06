

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
import os
from django.conf import settings

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
            
#             # Create a folder for the new user
#             user_folder = os.path.join(settings.MEDIA_ROOT, f"user_{user.id}")
#             os.makedirs(user_folder, exist_ok=True)
            
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['cpassword']

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already exists.")
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "Email already registered.")
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()

#                 # Create a folder for the new user
#                 user_folder = os.path.join(settings.MEDIA_ROOT, str(user.username))
#                 os.makedirs(user_folder, exist_ok=True)

#                 messages.success(request, "Account created successfully!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match.")
#     return render(request, 'accounts/signup.html')



# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['cpassword']

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already exists.")
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "Email already registered.")
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()

#                 # Create a folder for the new user
#                 user_folder = os.path.join(settings.MEDIA_ROOT, str(user.username))
#                 os.makedirs(user_folder, exist_ok=True)

#                 messages.success(request, "Account created successfully!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match.")
#     return render(request, 'accounts/signup.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if passwords match
        if password != request.POST['cpassword']:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            # Create a folder for the new user
            user_folder_path = os.path.join(settings.MEDIA_ROOT, 'user_folders', str(user.id))
            if not os.path.exists(user_folder_path):
                os.makedirs(user_folder_path)  # Creates the user's folder

            # Add success message
            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
    
    return render(request, 'accounts/signup.html')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.success(request, f"Welcome back, {user.username}!")
#             return redirect('home')  # replace with your app's home page URL
#         else:
#             messages.error(request, "Invalid credentials.")
    
#     return render(request, 'accounts/login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # or any page where you want to redirect after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')


def home(request):
    return render(request, 'accounts/home.html')