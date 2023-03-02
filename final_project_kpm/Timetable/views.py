from django.shortcuts import render
from Timetable.models import Student,Course,Subject,Assignment
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render (request, "index.html")

def login(request):
    if request.method == 'GET':
        data = Student.objects.filter(studentID = request.GET.get('s_id'))
        if len(data)==1:
            for value in data:

                if value.password == 'NULL' and request.GET.get('s_pass') == 'NULL':
                    dict={
                        'message':"Please Input Your ID Number",
                        'data': request.GET.get ('s_id'),
                    }
                    return render(request, 'signup.html', dict)

                elif value.password == request.GET.get('s_pass'):
                    if value.studentID == request.GET.get('s_id'):
                        return render(request, 'homepage.html')
                    else:
                        dict = {"message":""}
                        return render(request, "login.html", dict)
                    
                else:
                    dict={
                        'message':"- invalid password -"
                    }
                    return render(request, "login.html", dict)
            
        else:
            dict={
                'message': ""
            }
            return render (request, "login.html", dict)

def signup(request):
    if request.method == "GET":
        s_id = request.GET.get('studentID')
        s_name = request.GET.get('studentName')
        s_pass = request.GET.get('password')
        if s_id and s_name and s_pass:
            value = Student(studentID=s_id ,  studentName=s_name , password=s_pass)
            value.save()
            return render(request, "login.html")
        else :
            return render(request, "signup.html")
        

def homepage(request):
    return render(request,'homepage.html')

def searchSubject(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'searchSubject.html', context)

def list_subject(request):
    all_courses = Course.objects.all()

    if request.method == 'GET':
        course_code = request.GET.get('courseCode')
        if course_code:
            selected_course = Course.objects.get(courseCode=course_code)
            subjects = Subject.objects.filter(courseCode=selected_course)

            return render(request, 'list_subject.html', {
                'selected_course': selected_course,
                'subjects': subjects,
                'all_courses': all_courses,
            })

    return render(request, 'list_subject.html', {
        'all_courses': all_courses,
    })

def assignment(request):
    allsubject = Subject.objects.all()
    if request.method == 'POST':
        assignName = request.POST.get('assignName')
        dateOut = request.POST.get('dateOut')
        dateIn = request.POST.get('dateIn')
        submit = request.POST.get('submit')
        c_subject = request.POST.get('c_subject')

        if c_subject:
            # get foreign key data from reference table
            try:
                c_subject = Subject.objects.get(subjectCode=c_subject)
            except Subject.DoesNotExist:
                return HttpResponse('Invalid subject code')
            data = Assignment(assignName=assignName, dateOut=dateOut, dateIn=dateIn, submit=submit, subjectCode=c_subject)
            data.save()
            dict = {
                'allsubject': allsubject,
                'message': "Data Save"
            }
        else:
            dict = {
                'allsubject': allsubject,
                'error': "Subject code is required"
            }
    else:
        dict = {
            'allsubject': allsubject
        }

    return render(request, 'assignment.html', dict)


def list_assignment(request):
    all_subjects = Subject.objects.all()

    if request.method=='GET':
        subject_code = request.GET.get('subjectCode')
        assignments = Assignment.objects.filter(subjectCode__subjectCode=subject_code)
        number_assignments = assignments.count()
        context = {
            'assignments': assignments,
            'subject_code': subject_code,
            'number_assignments': number_assignments,
            'all_subjects': all_subjects,
        }
    else:
        context = {
            'all_subjects': all_subjects
        }

    return render(request, 'list_assignment.html', context)


def update_assignment(request,id):
    data = Assignment.objects.get(id=id)
    dict = {
        "data" : data
    }
    return render (request, "update_assignment.html", dict)

def save_update_assignment(request,id):
    assignment_submit = request.POST['submit']
    data=Assignment.objects.get(id=id)
    data.submit=assignment_submit
    data.save()
    return HttpResponseRedirect(reverse('list_assignment'))

def delete_assignment(request, id):
  data = Assignment.objects.get(id=id)
  data.delete()
  return HttpResponseRedirect(reverse('list_assignment'))
