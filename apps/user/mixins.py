from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

class LoginAndStaffMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')
    
class ValidateRequiredUsersPermissionsMixin(object):
    permission_required = ('user.view_user', 'user.add_user', 'user.delete_user', 'user.change_user')
    url_redirect = None
    
    """ Check if the permissions required are a tuple, if it ts, it is returned, otherwise it is converted """
    def get_perms(self):
        if isinstance(self.permission_required, str): return (self.permission_required)
        else: return self.permission_required 
        
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect
        
    """ Check if the user has the same permissions of permission_required, if he has it dispatch the request, otherwise the user its redirect to url_redirect (if it exists)  """
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'You do not have permissions to do this action')
        return  redirect(self.get_url_redirect())
    