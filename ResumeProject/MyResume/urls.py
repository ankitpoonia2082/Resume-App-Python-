from django.urls import path
from . import views

# application Urls

urlpatterns = [
    path('',views.about_view, name='about'),

    path('contact/', views.contact_view, name='contact'),

    path('skills/', views.skills_view, name='skills'),

    path('qualification/',views.qualification_view ,name='qualification'),

    path('project/',views.project_view , name='project'),

    path('experience/',views.experience_view , name='experience'),
]
