from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreateUserForm(UserCreationForm):
    # UserModel = get_user_model()
    

    class Meta:
        model = User
        fields = ['username', 'password1','password2']