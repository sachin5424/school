from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.response import Response
from .models import User
from django.shortcuts import redirect
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated   
# Create your views here.


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from .models import User,student
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
def new_account(request):
	
    if request.method =='POST':
    	
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        collge_group = request.POST.get('org_list')
        user=User(email=email,password=password1,username=username)
        user.save()
        add_group = Group.objects.get(id=collge_group)
        user.groups.add(add_group)
        login(request, user)
        return redirect('/')
    group = Group.objects.all()


    dis ={
      'group':group

    }
    return render(request,'student/createuser.html',dis)





from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
# from .model import student
@method_decorator(login_required, name="dispatch")
class student_list_view(ListView):
    model= student
    success_message = "%(username)s was created successfully"
    
 

@method_decorator(login_required, name="dispatch")
class student_list_view_update(UpdateView):
    model=student
    fields='__all__'
    success_url='/'
    success_message = 'Employee successful created'
    success_message = "%(username)s was created successfully"

@method_decorator(login_required, name="dispatch")
class student_list_view_delete(DeleteView):
    model=student
    success_url='/'


class student_list_create(CreateView):
    model=student
    fields='__all__'
    success_url='/'
