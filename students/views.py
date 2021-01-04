from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student

def reaStudentAll(request):
    students = Student.objects.order_by('-s_age')
    context = {
        'Students': students
    }
    return render(request, 'students/readStudents.html', context)

def regStudent(request):
    return render(request, 'students/registerStudent.html')

def regConStudent(request):
    student_name = request.POST['student_name']
    student_major = request.POST['student_major']
    student_age = request.POST['student_age']
    student_grade = request.POST['student_grade']
    student_gender = request.POST['student_gender']
    new_student = Student(s_name=student_name, s_major=student_major, s_age=student_age, s_grade=student_grade, s_gender=student_gender)
    new_student.save()
    return HttpResponseRedirect(reverse('students:stuAll'))

def detStudent(request, student_name):
    student = get_object_or_404(Student, s_name = student_name)
    context = {
        'Student': student
    }
    return render(request, 'students/readStudent.html', context)

def modStudent(request, student_name):
    student = get_object_or_404(Student, s_name = student_name)
    context = {
        'Student': student
    }
    return render(request, 'students/modifyStudent.html', context)

def modConStudent(request):
    student_name = request.POST['student_name']
    student = get_object_or_404(Student, s_name = student_name)
    student.s_major = request.POST['student_major']
    student.s_age = request.POST['student_age']
    student.s_grade = request.POST['student_grade']
    student.s_gender = request.POST['student_gender']
    student.save()
    return HttpResponseRedirect(reverse('students:stuDet', args=(student_name, )))

def delStudent(request, student_name):
    student = get_object_or_404(Student, s_name = student_name)
    student.delete()
    return HttpResponseRedirect(reverse('students:stuAll'))