from courses.models import Course,Module
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.shortcuts import render,redirect,get_object_or_404

from .forms import CourseEnrollForm,StudentWorkForm
from .models import StudentWork

def course_detail(request,course_id,module_id=None):
        course = get_object_or_404(Course,pk=course_id)
        modules = Module.objects.filter(course=course)
        if module_id:
            selected_module = get_object_or_404(Module,pk=module_id)
        else:
            selected_module = modules.first()
        studen_works = StudentWork.objects.filter(module=selected_module)if selected_module else[]
        if request.method == "POST":
            form =StudentWorkForm(request.POST,request.FILES)
            if form.is_valid():
                student_work = form.save(commit=False)
                student_work.module = selected_module
                student_work.save()
                return redirect('course_detail', course_id=course_id,module_id=selected_module.id)
        else:
            form =StudentWorkForm()
        return render(request,'students/course/course_detail.html',{
            'course' :course,
            'modules':modules,
            'selected_module':selected_module,
            'studen_works':studen_works,
            'form':form
        })
def edit_student_work(request,work_id):
        student_work =get_object_or_404(StudentWork,pk=work_id)
        if(request.method =="POST"):
            form = StudentWorkForm(request.POST,request.FILES,instance=student_work)
            if form.is_valid():
                    form.save()
                    return redirect('course_detail',course_id=student_work.module.course.id,module_id=student_work.module.id)            
        else:
            form = StudentWorkForm(instance=student_work)
        return render(request,'students/course/edit_student_work.html',{
            'form':form,
            'student_work': student_work
        })
    
def delete_student_work(request,work_id):
        student_work = get_object_or_404(StudentWork,pk=work_id)
        Course_id = student_work.module.course.id
        Module_id = student_work.module.id
        student_work.delete()
        return redirect('course_detail',course_id=Course_id,Module_id=Module_id)


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(
            username=cd['username'], password=cd['password1']
        )
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'student_course_detail', args=[self.course.id]
        )


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # get current module
            context['module'] = course.modules.get(
                id=self.kwargs['module_id']
            )
        else:
            # get first module
            context['module'] = course.modules.all()[0]
        return context



    

    
