from django.shortcuts import render

from myapp.models import UserData
from .utils import json_response


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def complete_registration(request):
    print('kjkj')
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_pic = request.FILES['profile_pic']
        user_data = UserData(name=name, age=age, address=address, phone=phone, email=email, profile_pic=profile_pic)
        user_data.save()
        return json_response(status=True, message="success")

    return json_response(status=False, message="Failed")

def view_user(request):
    user_data = UserData.objects.all()
    return render(request, 'myapp/view_users.html', {'user_data': user_data})