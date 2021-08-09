from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
import os
from .forms import RegisterForm, LoginForm
from .models import UserAvarta
from PIL import Image
fs = FileSystemStorage()

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        file = request.FILES.get('avarta')
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_created = form.save_user()
            if file != None and file.name != '':
                filepath =  os.path.join('static', file.name)
                saved_path = fs.save(filepath, file)
                im = Image.open(saved_path)
                im.save(saved_path, dpi=(600,600))
                UserAvarta.objects.create(user=user_created, avarta=saved_path)
            return redirect("index")
    return render(
        request=request,
        template_name="user/register.html",
        context={
            'form': form
        }
    )

def login_user(request):
    form = LoginForm()
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Hàm authenticate nhận username và password
            # Nếu thông tin đúng thì return User object
            # Không đúng thì return None
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user: # Kiễm tra not None là True
                # print("Thông tin gửi lên đúng")
                # Thông tin đúng. Phải giữ trạng thái đăng nhập của user
                # Dùng hàm login
                login(request, user) # Giữ đăng nhập
                # Thay vì redirect về index, phải kiễm tra cái tham số Get next
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return redirect("index")
            else:
                # print("THông tin sai")
                message = "Thông tin bạn nhập không đúng. Vui lòng nhập lại !"
    return render(
        request=request,
        template_name="user/login.html",
        context={
            'form': form,
            'message': message
        }
    )