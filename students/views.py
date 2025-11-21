from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Navbar Pages
def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# CRUD Views
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('home')
    return render(request, 'delete_student.html', {'student': student})
