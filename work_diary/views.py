from django.shortcuts import render , redirect
from django.contrib import messages
from .models import WorkDiary
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            work_diary = WorkDiary.objects.filter(user=request.user)
            return render(request , 'home.html',{'user_name': request.user.first_name,'work_diary':work_diary})
    
        elif request.method == "POST":
            hours = request.POST['hours']
            date = request.POST['date']
            work_diary = WorkDiary.objects.create(user=request.user , date=date , hours_worked=hours)
            return redirect('/')
    else:
        return redirect('/users/login')

def delete_work(request , work_id=None):

    if not work_id:
        return redirect('/')
    else:
        WorkDiary.objects.filter(id=work_id , user=request.user).delete()
        return redirect('/')