from .form import CreateUserForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CreateUserForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')