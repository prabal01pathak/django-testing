from django.db import models

# Create your models here.


class Course(models.Model):
    # image = models.ImageField(upload_to=course_image_path, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    register = models.TextField(null=True)
