from django.urls import path
from .views import resume_view, ContactCreateView

urlpatterns = [
    path('resume/', resume_view, name='resume'),
    path('contact/', ContactCreateView.as_view(), name='contact_me')
]