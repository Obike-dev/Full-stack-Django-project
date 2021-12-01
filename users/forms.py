from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from users.models import UserProfile

GENDER = [ ('Male', 'Male'), ('Female', 'Female'), ('Not specified', 'Rather not say') ]

User._meta.get_field('email')._unique = True

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class':'username-field signup-fields', 
            'type':'text', 
            'align':'center', 
            'placeholder':'username'}),
    )
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class':'email-field signup-fields', 
            'type':'email', 
            'align':'center', 
            'placeholder':'email'}),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class':'password1-field signup-fields', 
            'type':'password', 
            'align':'center', 
            'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            'class':'password2-field signup-fields', 
            'type':'password', 
            'align':'center', 
            'placeholder':'password confirmation'}),
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'username-field'}),
        
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'username',
                'class':'username-email-login_field',
                'align':'center',
            }
        )
    )

    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'password',
                'class':'password-login-field',
                'type':'password', 
                'align':'center', 


            }
        )
    )

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            'class':'username', 
            'type':'text', 
            'align':'center', 
            'placeholder':'username'}),
    )
    email = forms.CharField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            'class':'email-field signup-fields', 
            'type':'email', 
            'align':'center', 
            'placeholder':'email'}),
    )
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(
        required=False,     
        label = "Profile photo",
        help_text="change profile photo",
        widget=forms.FileInput(attrs={
            'class':'file-img'
            
        })
    )
    
    bio = forms.CharField(
        required=False,     
        widget=forms.Textarea(
            attrs={
                # 'id':'txtinput',
                'class':'edit-user-txtarea',
                'rows':5,
              
            }
        )
    )
    
    website = forms.URLField(
        label="",
        required=False,
        widget=forms.URLInput(attrs={
            'class':'', 
            'type':'url', 
            'align':'center', 
            'placeholder':'Website'}),
    )
    gender = forms.ChoiceField(
        required=False,    
        choices= GENDER,
        label="",
        widget=forms.Select(attrs={
            'class':'', 
            'type':'text', 
            'align':'center',}),
    )
    
    class Meta:
        model = UserProfile
        fields = ['image','bio','website','gender']
    


class ChangeUserPassword(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type':'password', 
            'align':'center', 
        }),
    )
    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type':'password', 
            'align':'center', 
           }),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'type':'password', 
            'align':'center', 
        }),
    )
    
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
    
















