from django import forms
from .models import Folder,File

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input w-full border-gray-300 rounded-lg p-2'})
        }

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        max_size = 40 * 1024 * 1024  # 40MB
        if file.size > max_size:
            raise forms.ValidationError("File size exceeds the 40MB limit.")
        return file