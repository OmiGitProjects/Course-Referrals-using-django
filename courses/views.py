from django.shortcuts import render, redirect
from .models import Course
from profiles.models import Profile, Company_Bank, Referrel_key, MainMembershipModelTable, level_Percentage

import random

def courses(request):

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
    else:
        profile = ''

    bank = Company_Bank.objects.get(id=1)

    courses = Course.objects.all()
    context = {'courses': courses, 'profile': profile, 'CBank': bank}
    return render(request, 'courses/index.html', context)

def referrals_code_page(request, *args, **kwargs):
    course_id = kwargs.get('course_id')
    course = Course.objects.get(id=course_id)

    profile = Profile.objects.get(user=request.user)

    for key in profile.referrel_keys.all():
        if key.course == course:
            referral_key_obj = key
        else:
            key = None

    context = {'profile': profile, 'key': referral_key_obj, 'course': course}
    return render(request, 'courses/referral_key.html', context)
    

def buy_course(request, *args, **kwargs):

    course_id = kwargs.get('course_id')
    course = Course.objects.get(id=course_id)
    profile = Profile.objects.get(user=request.user)
    bank = Company_Bank.objects.get(id=1)

    context = {'course': course,'profile': profile, 'CBank': bank}
    return render(request, 'courses/payment.html', context)


# ************************* MLM Concept Function ************************* 

def add_main_memberModel(profile_referror, profile_user, level=1):
    profile_referror.recommanded_len += 1

    # level = level_Percentage.objects.all()

    profile_referror.recommanded_to.add(profile_user.user)
    profile_referror.save()

    MainModel_obj = MainMembershipModelTable(new_user=profile_user, recommand_by=profile_referror)
    MainModel_obj.save()

    return True

def course_purchased(request, *args, **kwargs):
    
    if request.method == "POST":
        price = float(request.POST.get('price'))
        course = request.POST.get('course')
        author = request.POST.get('author')

        referral_code_course = request.POST.get('referral_code')
        
        if referral_code_course:
            
            while True:
                referral_key_obj = Referrel_key.objects.get(referral_key=referral_code_course)
                referror = referral_key_obj.user
                profile_referror = Profile.objects.get(user=referror)
                
                user = request.user
                profile_user = Profile.objects.get(user=user)

                if profile_referror.recommanded_len <= 3:
                    is_save = add_main_memberModel(profile_referror, profile_user)

                    if is_save:
                        break
                else:
                    recommanded_ids = profile_referror.recommanded_to.all()

                    # for profile in recommanded_ids:
                    #     if profile.recommanded_len <= 3:
                    #         is_save = add_main_memberModel(profile_referror, profile_user, level=2)
                    #         profile.recommanded_len += 1
                    
        # Operations 
        
        # Finding in Database
        profile = Profile.objects.get(user=request.user)
        course = Course.objects.get(id=course)

        wallet_price = profile.wallet
        new_price = wallet_price - price
        profile.wallet = new_price
        
        course.purchased.add(request.user)
        
        bank = Company_Bank.objects.get(id=1)
        bank.price += price

        any_num = random.randint(1000, 99999999)
        referral_code = f'{str(request.user)}{str(course.title)}{str(profile.referral_code)}{str(any_num)}'
        referral_obj = Referrel_key(user=request.user, course=course, referral_key=referral_code)
        referral_obj.save()
        profile.referrel_keys.add(referral_obj)
        
        # Saving All databases
        course.save()
        bank.save()
        profile.save()

        return redirect('course-page')

# ****************************** END MLM ***************************