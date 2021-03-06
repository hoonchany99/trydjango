from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from .models import Course 
from .forms import CourseModelForm

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course,id = id)
        return obj



class CourseUpdateView(CourseObjectMixin,View):
    template_name = 'courses/course_update.html'
    def get_object(self):
        id = self.kwargs.get("id")
        obj = None
        if id is not None:
            obj = get_object_or_404(Course,id = id)
        return obj

    def get(self, request, id = None, *args, **kwargs):
        context=  {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance = obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id = None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST , instance = obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class CourseCreateView(CourseObjectMixin,View):
    template_name = 'courses/course_create.html'
    def get(self,request,*args, **kwargs):
        form = CourseModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form":form}
        return render(request, self.template_name, context)

class CourseView(CourseObjectMixin,View):
    template_name = 'courses/course_detail.html'
    def get(self, request,id = None ,*args, **kwargs):
        context=  {}
        if id is not None:
            obj = get_object_or_404(Course, id = id)
            context['object'] = obj
        return render(request, self.template_name, context)


# HTTP METHODS
def my_fbv(request,*args, **kwargs):
    return render(request, 'about.html', {})  

