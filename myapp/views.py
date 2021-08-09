from os import stat_result
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http.response import JsonResponse
import time
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from .models import Reporter, Article
from .forms import ReporterForm, ArticleForm, RegisterForm

# Create your views here.
# MVT thì V nó views (ngang với chữ C trong mô hình MVC)
def index(request): # Tham số bắt buộc phải có của các hàm trong views.py 
    # là resquest: HttpRequest
    # print(request.GET['name']) # request.GET nó nằm trên url khi mình gõ
    # name = request.GET.get('name','') # request.GET là 1 dạng như dictionary
    # print(name)
    # # .get() -> có key thì lấy giá trị, ko thì lấy giá trị default
    # request.session['name'] = name # Lưu vào session (trên cùng 1 phiên làm việc)
    # response = HttpResponse()
    # response.write("<h1> Hello From Django Web</h1>")
    # response.write("Đây là app đầu tiên")
    # print(request.POST.get('fname',''))
    # print(request.POST.get('lname',''))
    # age = 12
    # name = "Alice"
    # lst = ["Python", "Django", "Online", "Zoom Meeting"]
    # all_reporters = Reporter.objects.all()

    return render(
        request=request,
        template_name="index.html"
    )

#R
def list_reporter(request):
    # Lấy user logged
    user = request.user
    print(user.get_user_permissions())
    all_reporters = Reporter.objects.all()
    paginator = Paginator(all_reporters, settings.PAGINATE_BY)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    search = request.GET.get('search')
    if search:
        page_obj = Reporter.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        # print(all_reporters)
    return render(
        request=request,
        template_name="reporter/list.html",
        context={
            'page_obj': page_obj
        }
    )

def search_reporter(request):
    search = request.GET.get('search')
    if search:
        all_reporters = Reporter.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        print(all_reporters)
    else:
        all_reporters = []
    results = []
    for item in all_reporters:
        results.append({
            "first_name": item.first_name,
            "last_name": item.last_name,
            "email": item.email,
        })
    time.sleep(3)
    return JsonResponse({
        "status": 200,
        "message": results
    })

#C
@login_required(login_url="/login") # Đặt decorator `login_required` bắt buộc người dùng phải đăng nhập
# login_url để dẫn tới trang login
def add_reporter(request):
    reporter_form = ReporterForm()
    if request.method == "POST":
        # print(request.POST)
        reporter_form = ReporterForm(request.POST)
        if reporter_form.is_valid():  # hàm is_valid() nó gọi tất cả các hàm mà bắt đầu là clean_
            # print("Form validate OK")
            # data = reporter_form.cleaned_data # cleaned_data trong sau is_valid. 
            reporter_form.save()
            return redirect("index")
    return render(
        request=request,
        template_name='reporter/add.html',
        context={
            'form': reporter_form
        }
    )

# R
@login_required(login_url="/login") # Đặt decorator `login_required` bắt buộc người dùng phải đăng nhập
# login_url để dẫn tới trang login
def view_detail_reporter(request, reporter_id):
    reporter_data = Reporter.objects.get(id=reporter_id)
    return render(
        request=request,
        template_name="reporter/detail.html",
        context={
            'reporter': reporter_data
        }
    )

#U
@login_required(login_url="/login") # Đặt decorator `login_required` bắt buộc người dùng phải đăng nhập
# login_url để dẫn tới trang login
def update_reporter(request, reporter_id):
    reporter_data =  get_object_or_404( Reporter, id=reporter_id) # = Reporter.objects.get(id=reporter_id)
    reporter_form = ReporterForm(instance=reporter_data)
    if request.method == "POST":
        # print("Form validate OK")
        reporter_data.first_name = request.POST.get('first_name',reporter_data.first_name)
        reporter_data.last_name = request.POST.get('last_name',reporter_data.last_name)
        reporter_data.email = request.POST.get('email',reporter_data.email)
        reporter_data.save()
        return redirect("index")
    return render(
        request=request,
        template_name="reporter/update.html",
        context={
            'form': reporter_form
        }
    )

#D
@login_required(login_url="/login") # Đặt decorator `login_required` bắt buộc người dùng phải đăng nhập
# login_url để dẫn tới trang login
def delete_reporter(request, reporter_id):
    reporter_data =  get_object_or_404( Reporter, id=reporter_id) # = Reporter.objects.get(id=reporter_id)
    reporter_data.delete()
    return redirect("index")


def add_article(request):
    form_article = ArticleForm()
    if request.method == "POST":
        # print(request.POST)
        form_article = ArticleForm(request.POST)
        if form_article.is_valid():  # hàm is_valid() nó gọi tất cả các hàm mà bắt đầu là clean_
            # print("Form validate OK")
            # data = form_article.cleaned_data # cleaned_data trong sau is_valid. 
            form_article.save()
            return redirect("index")
    return render(
        request=request,
        template_name='article/add.html',
        context={
            'form': form_article
        }
    )


def validate_email(request):
    if request.method == "POST":
        try:
            input_email = request.POST['email']
            Reporter.objects.get(email=input_email)
        except Reporter.DoesNotExist:
            return JsonResponse({
                "status": 200,
                "message": f"Bạn có thể sử dụng {input_email} này"
            })
        return JsonResponse({
            "status": 500,
            "message": f"Email {input_email} này đã tồn tại. Vui lòng chọn email khác"
        })

def validate_username(request):
    if request.method == "POST":
        try:
            input_username = request.POST['username']
            User.objects.get(username=input_username)
        except User.DoesNotExist:
            return JsonResponse({
                "status": 200,
                "message": f"Bạn có thể sử dụng {input_username} này"
            }, status = 200)
        return JsonResponse({
            "status": 500,
            "message": f"Username {input_username} này đã tồn tại. Vui lòng chọn username khác"
        }, status=409)
# Thứ tự tạo mới 1 hàm trong views.py
# Step 1: Viết hàm. Chọn template hiển thị
