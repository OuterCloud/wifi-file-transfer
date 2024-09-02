"""views.py"""

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def upload_file(request):
    """Upload a file"""
    if request.method == "POST" and request.FILES["file"]:
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        return HttpResponse("File uploaded successfully")
    return render(request, "upload.html")
