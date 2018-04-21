from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

# logging out the user
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
