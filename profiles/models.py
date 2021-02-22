from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Referrel_key(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    referral_key = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.referral_key)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userPlanA_id = models.CharField(max_length=100, blank=True)
    userPlanB_id = models.CharField(max_length=300, blank=True)
    is_mentor = models.BooleanField(default=False)
    is_master_mentor = models.BooleanField(default=False)
    recommanded_len = models.IntegerField(default=0)
    recommanded_to = models.ManyToManyField(User, blank=True, related_name='recommand_to')
    referrel_keys = models.ManyToManyField(Referrel_key, blank=True)
    level = models.IntegerField(default=1)
    wallet = models.FloatField(default=0.00)
    referral_code = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)


    def get_all_referral_keys(self):
        return self.referrel_keys.all()

class UserCounter(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    user_id_number = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Plan_A_Model(models.Model):
    user = models.ForeignKey(UserCounter, on_delete=models.CASCADE, blank=True)
    Id_number = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class MainMembershipModelTable(models.Model):
    new_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='new_user')
    recommand_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.new_user)


class Company_Bank(models.Model):
    price = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.price)

class level_Percentage(models.Model):
    level_name = models.IntegerField(blank=True)
    percentage = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.level_name)