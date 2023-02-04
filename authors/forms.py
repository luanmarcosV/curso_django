from django import forms
from django.contrib.auth.models import User

def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val

class RegisterForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password'
        }),
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        })
    )
    
    class Meta:
        
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'E-mail',
            'password': 'Password',
            'password2': 'Confirm your password',
        }
        
        help_texts = {
            'email': 'The e-mail must be valid.',
        }
        
        error_messages = {
            'username': {
                'reqired':'Username is required',
            }
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here',
                
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here',
            })
            
        }