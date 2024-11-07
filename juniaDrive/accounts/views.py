

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
import os
from django.conf import settings
from .models import Folder, File
from .forms import FolderForm 
from .forms import FileUploadForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse  # Add this import


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


# def home(request):
#     return render(request, 'accounts/home.html')


# def home(request):
#     # Ensure the user is authenticated
#     if request.user.is_authenticated:
#         folders = Folder.objects.filter(user=request.user)
#     else:
#         folders = []
    
#     return render(request, 'accounts/home.html', {'folders': folders})

@login_required(login_url='login')  # Ensures only logged-in users can access this view
def home(request):
    # Check if the user is authenticated before querying
    if not request.user.is_authenticated:
        return redirect('login')

    # Now it’s safe to retrieve folders for the authenticated user
    folders = Folder.objects.filter(user=request.user)
    return render(request, 'accounts/home.html', {'folders': folders})


# here
def folder_list(request):
    folders = Folder.objects.filter(user=request.user)
    return render(request, 'accounts/folder_list.html', {'folders': folders})

def upload_file(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, user=request.user)
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        
        # Enforce file size and storage limits here
        max_file_size = 40 * 1024 * 1024
        if uploaded_file.size > max_file_size:
            messages.error(request, "File too large! Maximum size is 40MB.")
            return redirect('folder_list')

        # Create a new File object
        File.objects.create(
            name=uploaded_file.name,
            folder=folder,
            file=uploaded_file,
            size=uploaded_file.size,
        )
        messages.success(request, "File uploaded successfully.")
        return redirect('folder_list')

    return render(request, 'accounts/upload_file.html', {'folder': folder})



def file_upload(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, user=request.user)
    
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            max_file_size = 40 * 1024 * 1024  # 40 MB limit
            
            # Check if file size exceeds limit
            if uploaded_file.size > max_file_size:
                messages.error(request, "File too large! Maximum size is 40MB.")
                return redirect('folder_detail', folder_id=folder.id)

            # Save file with FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            
            # Create File object
            File.objects.create(
                name=filename,
                folder=folder,
                file=uploaded_file,
                size=uploaded_file.size
            )
            messages.success(request, "File uploaded successfully.")
            return redirect('folder_detail', folder_id=folder.id)

    return render(request, 'accounts/upload_file.html', {'folder': folder})


# def folder_detail(request, folder_id):
#     folder = get_object_or_404(Folder, id=folder_id, user=request.user)
#     files = folder.files.all()  # Assuming a `related_name='files'` in the File model
#     return render(request, 'accounts/folder_detail.html', {'folder': folder, 'files': files})

MAX_UPLOAD_SIZE = 40 * 1024 * 1024  # 40 MB

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, user=request.user)
    files = folder.files.all()
    
    file_previews = []
    for file in files:
        preview_type = None
        if file.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
            preview_type = 'image_preview'
        elif file.name.endswith('pdf'):
            preview_type = 'pdf_preview'
        elif file.name.endswith(('mp3', 'wav', 'ogg')):
            preview_type = 'audio_preview'
        elif file.name.endswith(('mp4', 'avi', 'mov')):
            preview_type = 'video_preview'
        elif file.name.endswith(('txt', 'html', 'py', 'js', 'css')):
            preview_type = 'text_preview'
        
        file_previews.append({'file': file, 'preview_type': preview_type})

    return render(request, 'accounts/folder_detail.html', {'folder': folder, 'file_previews': file_previews})


def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user  # Assign folder to the logged-in user
            folder.save()
            return redirect('home')  # Redirect to home after creating folder
    else:
        form = FolderForm()
    return render(request, 'accounts/create_folder.html', {'form': form})


def upload_file(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, user=request.user)
    
    if request.method == 'POST':
        if 'file' in request.FILES:
            uploaded_file = request.FILES['file']
            max_file_size = 40 * 1024 * 1024  # 40 MB
            
            # Check file size
            if uploaded_file.size > max_file_size:
                messages.error(request, "File too large! Maximum size is 40MB.")
                return redirect('folder_detail', folder_id=folder.id)

            # Save file
            File.objects.create(
                name=uploaded_file.name,
                folder=folder,
                file=uploaded_file,
                size=uploaded_file.size
            )
            messages.success(request, "File uploaded successfully.")
            return redirect('folder_detail', folder_id=folder.id)

    # Render the upload file template
    return render(request, 'accounts/upload_file.html', {'folder': folder})


def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id, folder__user=request.user)

    # Construct the file path manually using MEDIA_ROOT
    file_path = os.path.join(settings.MEDIA_ROOT, file.file.name)

    # Delete the file from storage and the database
    if os.path.exists(file_path):
        os.remove(file_path)  # Manually remove the file from the filesystem
    file.delete()  # Delete the record from the database

    messages.success(request, "File deleted successfully.")
    # Redirect back to the folder detail page after deletion
    return HttpResponseRedirect(reverse('folder_detail', args=[file.folder.id]))