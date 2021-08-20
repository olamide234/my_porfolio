from django.shortcuts import render
from .models import Contact
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def resume_view(request):
    return render(request, 'core/resume.html')

class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    fields = ['full_name', 'email', 'message']
    template_name = "core/contact_form.html" #default template name here is contact_form which is preferred because there's anpother 
    #view called update view that also needs the template
    # send back to resum page on successful save
    success_message = 'Message Sent!'
    success_url = reverse_lazy('resume')