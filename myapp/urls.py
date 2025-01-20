from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index_page,name='index'),
    path('signup_login/',views.signup_login,name='signup_login'),
    path('login/',views.login,name='login'),
    path('course/',views.viewCourse,name='course'),
    path('about/',views.about,name='about'),
    path('chart/<int:id>',views.viewChart,name='chart'),
    path('blog/<int:id>',views.blog,name='blog'),
]