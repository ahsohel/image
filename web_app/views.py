from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import image_up
# Create your views here.

def index(request):



    return render(request, 'index.html')
def save_our_files(request):

    variable_1 = request.FILES['logo']

    fs = FileSystemStorage()
    filename = fs.save(variable_1.name, variable_1)
    uploaded_file_url = fs.url(filename)
    print(filename)

    variable_2 = request.FILES['benner']

    fss = FileSystemStorage()
    filename2 = fss.save(variable_2.name, variable_2)
    uploaded_file_url2 = fss.url(filename2)
    print(filename2)

    s_table_file = image_up(name="sohel", image_logo=uploaded_file_url, image_benner=uploaded_file_url2)
    s_table_file.save()
    return render(request, 'index.html')
