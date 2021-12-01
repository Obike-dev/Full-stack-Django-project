from django.contrib import messages
from users.forms import LoginForm
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView

from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django import template

from django.contrib.auth import update_session_auth_hash

from django.shortcuts import get_object_or_404, redirect, render
from users.forms import RegisterForm,UpdateProfileForm,UpdateUserForm,ChangeUserPassword
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from shoes_app.models import Shoe

def sign_up(request):
      
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account with the username {username} has been created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/sign_up.html',{'form':form})


class Profile(LoginRequiredMixin,DetailView):
        
    template_name = 'users/user_profile.html'
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['users'] = User.objects.all()
        context_data['shoes'] = Shoe.objects.all().order_by('-time_posted')
        return context_data

    def get_object(self):
           UserName= self.kwargs.get("username")
           return get_object_or_404(User, username=UserName)

  
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    

@login_required
def update_profile(request,username):
    user = User.objects.get(username=username)
    
    if user.id != request.user.id:
        return redirect('index')
    
    if request.method == 'POST':    
        user_form = UpdateUserForm(request.POST,instance=user)
        profile_form = UpdateProfileForm(request.POST,request.FILES,
        instance=user.userprofile)
    
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile has been updated successfully')
            return redirect('index')
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=user.userprofile)
    
    return render(request,'users/update_profile.html',
    {'user_form':user_form, 'profile_form':profile_form})


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data)|Q(username=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					plaintext = template.loader.get_template('users/password_reset_email.txt')
					htmltemp = template.loader.get_template('users/password_reset_email.html')
					c = { 
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					text_content = plaintext.render(c)
					html_content = htmltemp.render(c)
					try:
						msg = EmailMultiAlternatives(subject, text_content, 'Website <admin@example.com>', [user.email], headers = {'Reply-To': 'admin@example.com'})
						msg.attach_alternative(html_content, "text/html")
						msg.send()
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.info(request, "Password reset instructions have been sent to the email address entered.")
					return redirect ("index")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})




@login_required
def change_password(request,username):
    
    user = User.objects.get(username=username)
    
    if user.id != request.user.id:
        return redirect('/')
    
    if request.method == 'POST':
        form = ChangeUserPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
    else:
        form = ChangeUserPassword(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required
def delete_user(request,username):
    user = User.objects.get(username=username)
    
    if user.id != request.user.id:
        return redirect('index')
    
    if request.method == 'GET':
        return redirect('index')
    
    if request.method == 'POST':
        user.delete()
        return redirect('index')
    
    return render(request,'users/delete_account.html',{'user':user})
    
    







