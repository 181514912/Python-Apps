from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

# logging out the user
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

# register a new user
def register(request):
    if request.method!='POST':
        form=UserCreationForm() # displaying a blank registeration form
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user=form.save()
            # loging the user in and redirecting to home page
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context={'form':form}
    return render(request,'users/register.html',context)        
