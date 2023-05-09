from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def allStudent(request):
     myvars = {
        'fname': 'saror',
        'lname': 'Essa',
        'mylist': [1, 2, 3, 4, 5, 6, 7, 8],
        'mydict': {'python': 'django'}
    }
     return render(request, 'student/student.html', context=myvars)

def addStudent(request):
    return render(request, 'student/add.html')

def editStudent(request):
    return render(request, 'student/edit.html')
