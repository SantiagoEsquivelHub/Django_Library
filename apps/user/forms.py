from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import * 

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Name of user'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        
        
class UserForm(forms.ModelForm):
    """ 
    User Registration Form 
    
    Variables:
    
    password1: Password
    password2: Password verification
    
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'id': 'password1',
            'required': 'required'
        }
    ))

    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter (again) your password',
            'id': 'password2',
            'required': 'required'
        }
    ))
    
    class Meta():
        model = User
        fields = ['email', 'username', 'name', 'last_name']
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Enter your email',
                }
            ),
            'name': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Enter your names',
                }
            ),
            'last_name': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Enter your last names'
                }
            ),
            'username': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Enter your user name',
                }
            ),
        }
        
    def clean_password2(self):
        """ 
        Password validation. 
        
        Method that validates that both password are equals, before to be encrypted and stored in database. Returns le valide password.
        
        Exceptions:
        - ValidationError = When the passwords are not equals show an error message
        
        cleaned_data returns a dictionary of validated form input fields and their values
        """
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match!')
        return password2
    
    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password1'))
        
        if commit:
            user.save()
        return user 
    