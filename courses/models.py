from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True)
    purchased = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return str(self.title)

    def get_course_purchased_list(self):
        return self.purchased.all()