from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    teacher_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='teacher')
    student_ids = models.ManyToManyField(User, related_name='students')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title



