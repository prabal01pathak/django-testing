from django.shortcuts import render, get_object_or_404
from .models import Course


def register_course(request, id):
    if request.method == "POST":
        course_id = id  # Assuming you have a form field with the name 'start_course'
        course = get_object_or_404(Course, pk=course_id)
        print("course is: ", course)
        course.register = "Yes"
        course.save(update_fields=["register"])
    return render(request, "profile.html")
