from django.urls import path
from .import views

urlpatterns = [
    path('', views.courses, name='course-page'),
    path('buy_course/<str:course_id>', views.buy_course, name='buy_course'),
    path('course_purchased/', views.course_purchased, name='course_purchased'),
    path('share/referral/<str:course_id>', views.referrals_code_page, name='referral_home')
]
