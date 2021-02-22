from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Plan_A_Model, UserCounter

from django.utils.crypto import get_random_string
import random

@receiver(post_save, sender=User)
def create_user_post_save(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)

        user_counter = UserCounter.objects.create(user=profile)
        user_id_number = random.randint(10000, 99999999)

        try:
            user_counter_obj = UserCounter.objects.all()
            for user in user_counter_obj:
                if user.user_id_number == user_id_number:
                    user_id_number = random.randint(10000, 99999999)
        finally:
            user_counter.user_id_number = user_id_number
            user_counter.save()

        plan_a = Plan_A_Model.objects.create(user=user_counter)
        userid_number = plan_a.user.user_id_number

        planA_id_number = str(userid_number) + '-PlanA-' + str(plan_a.id)
        plan_a.Id_number = planA_id_number
        plan_a.save()

        profile.userPlanA_id = planA_id_number
        profile.referral_code = get_random_string(length=16)
        profile.save()